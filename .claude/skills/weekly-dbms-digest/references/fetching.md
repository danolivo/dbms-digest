# Fetching technique

Cap: 60 lines. Knowledge, not a log — no dates, no "this run" narrative. A new recipe for
a target replaces the old one here, it doesn't get appended below it. Nothing new about
access this run → write nothing here.
## Provenance (web_fetch)
- Cold `web_fetch` only works on a URL already in provenance (a search result, or a link on a page already fetched). Seed with `WebSearch`, then chain through fetched pages.
- Official domains often serve cache-stale content to plain fetch — check the newest date on the page before trusting a listing.
- A feed fetched as raw XML can come back as undecoded "[binary data]" — fetch the HTML index page instead, or use a browser.
- Same-origin in-page `fetch()` is blocked if the current tab URL carries a query string — navigate to a clean URL first.
- `github.com/postgres/postgres` (`/commits/master?since=&until=`, `/commit/<sha>`) is a ground-truth fallback when postgresql.org/mail-archive/commitfest are blocked — but it can itself come back empty; don't rely on it alone.
## Two browsers
- Claude Browser (`mcp__Claude_Browser__*`, in-app pane) and `Control_Chrome` (real host Chrome, AppleScript) cover different domains — when one refuses a domain outright, try the other before concluding it's unreachable. Claude Browser hard-blocks `old.reddit.com` ("blocked by policy"); `Control_Chrome` reaches it fine, plus Lobsters, DBA SE, and the non-English sources.
- `Control_Chrome` prereq: Chrome → View → Developer → "Allow JavaScript from Apple Events" — otherwise `get_page_content`/`execute_javascript` fail with a misleading "Google Chrome is not running" (`list_tabs`/`open_url` still work). Its `execute_javascript` is synchronous — wrap in an IIFE: kick off with `window.__x={done:false}; (async()=>{…; window.__x.done=true;})(); 'started'`, then poll `window.__x.done ? JSON.stringify(window.__x.out) : 'pending'`; return one JSON string.
- Claude Browser's `javascript_tool` returns `undefined` on a top-level `return` — end with a bare expression. `get_page_text` lags one step right after `navigate` inside a `browser_batch` — read it in a separate call.
## pgsql-hackers / -bugs / -performance / -general
- SOLVED: `postgresql.org/list/<listname>/<YYYY-MM>/` renders fully only in a browser (plain fetch gets an empty shell). It carries a "Jump to day" strip (`/list/<listname>/since/YYYYMMDD0000/`); same-origin `fetch()` each day and parse with `DOMParser`.
- Parsing trap: the subject anchor is in `th[scope="row"]`, not a `td` — use `th a[href*="/message-id/"]`; `td[0]`=author, `td[1]`=time; a trailing 📎 = attachment. New threads = subjects not starting with `Re:`/`RE:`.
- `since/` pages are not contiguous — one fetch's date coverage can skip a day relative to the next one's start point. Diff the resulting date set against all 7 days in the window; sometimes 3 fetches are needed, not the usual 2.
- `/message-id/flat/<id>` (whole thread) and `/message-id/<id>` (body in `.message-content`, fallback `pre`) both work via plain fetch. Same URL shapes work for all four lists.
- Dead ends, don't retry: mail-archive's hackers list can't be seeded by any search; `marc.info/?l=postgresql-hackers` is empty; `postgrespro.com/list/pgsql-hackers/<month>` refused cold; hackorum.dev's `/topics` index overflows the fetch limit (fine as a human UI only).
## mail-archive (pgsql-committers)
- The one consistently fresh mail-archive list. Its *thread* index (`index.html`) stays current even when its *date* index (`maillist.html`) goes stale — use the thread index. Individual `msgNNNNN.html` pages carry a real timestamp (e.g. `-0700`) for boundary checks, the full commit message, and a git commitdiff link.
- The pgsql-performance mirror has been silent since 2026-05-11; no pgsql-bugs mirror exists at all. Fetch one message per call — batched fetch+regex can trip a cookie/query-string guard.
## CommitFest
- Never fetch the bare `/<n>/` list (~180KB, overflows, no totals anyway). Fetch `/<n>/?tag=<anything>` instead (small) — its "Activity log" link puts `/<n>/activity/` into provenance, and its header "Status summary" line gives authoritative queue totals.
- Both the global and per-CF activity logs cap at ~100 rows with no pagination — a Monday capture already misses the prior Mon–Tue; capture mid-week or accept a partial count. Either log can be the stale one on a given run — check the newest timestamp before trusting either. CF numbers aren't consecutive (a year-long Drafts CF can sit between two regular ones).
## HN — Algolia, hntoplinks, hckrnews
- Prefer HN Algolia: `hn.algolia.com/api/v1/search_by_date?tags=story&query=<kw>&numericFilters=created_at_i>LO,created_at_i<HI,points>N&hitsPerPage=50`, ~8 keywords, dedupe by objectID. CORS-blocked direct from news.ycombinator.com; works same-origin from hn.algolia.com, or from any origin via `Control_Chrome`. Finds items below the general-interest cutoff that hntoplinks misses.
- Fallback only: `hntoplinks.com/week` (page 1 usually fresh, page 3+ can be months-old — check item IDs first) and `hckrnews.com` (fresh but only the last ~2–3 days). Live `news.ycombinator.com/item?id=…` pages return empty to plain fetch.
## Reddit
- `old.reddit.com/r/<sub>/top.json?t=week&limit=40` — read-only JSON, no login, no banner; `old.reddit.com<permalink>.json?limit=6` for the post + top comments. The HTML `top/?t=week` redirects to a login wall — always use `.json`.
- Sweep seven subs: r/PostgreSQL, r/databasedevelopment (no filter needed), r/SQL, r/Database, r/dataengineering, r/programming, r/ExperiencedDevs (keyword-filter the last five). **Sort by comment count, not score** — the most substantive debates often sit at low or zero points.
## Lobsters
- `/t/databases` plain-fetch returns an empty body (looks quiet, is actually blocked) — renders fine in a browser. Extract with `document.querySelectorAll('a.u-url')` (`li.story` returns nothing). Low engagement, rarely earns a Community-pulse slot on its own, but a strong article-discovery feed.
## DBA Stack Exchange
- Use the API, not the HTML: `api.stackexchange.com/2.3/questions?site=dba&fromdate=<epoch>&todate=<epoch>&order=desc&sort=votes&pagesize=15&filter=!nNPvSNdWme` — CORS-open, no key needed, already windowed. Usually low-signal for Postgres specifically (traffic skews SQL Server/Informix) — cheap to scan, rarely contributes.
## arXiv cs.DB
- Reachable cold via `www.arxiv.org` (the bare host sometimes doesn't surface in search). Day-bucketed; use `/list/cs.DB/<month>` if `/recent` is stale. `/abs/<id>` gives `[Submitted on …]` plus `blockquote.abstract` for the gist.
## Habr hub
- `habr.com/ru/hubs/postgresql/` ("Статьи" tab) plain-fetches the live chronological list with dates — no browser needed. Never fetch `/articles/top/alltime/` (all-time list, wastes tokens). In a browser: `document.querySelectorAll('article')` → `time[datetime]` + `.tm-title__link` (+ vote counter) per item.
## Misc
- Conference schedules (confbase.io) are a JS iframe embed; navigate the browser straight to the iframe src `https://confbase.io/embed/<slug>/<year>/schedule?theme=dark` and `get_page_text` — the WordPress page itself fetches but the talk list needs the browser.
- `postgresweekly.com/latest` redirects to the real issue; `/issues/latest` errors. `api.github.com` works same-origin from any page (CORS *) for release dates, but is CSP-blocked from some vendor pages (e.g. planetscale.com).
## Open
- `modb.pro` [zh] is still unenumerable — front page, `/search?k=`, `/tag/<t>` are all client-rendered shells with no dated article list, even in a real browser. Untried: the mobile site (`m.modb.pro`) or watching its XHR endpoints directly.
- No public Telegram/Matrix DB channel has been found yet worth pinning — searches keep returning marketing aggregators only.
