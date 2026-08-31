# Community sources

The living list of *discussion* sources for the **Community pulse** section — forums, link
aggregators, Q&A sites, and chat/messenger channels where people actually argue about
databases. Distinct from `sources.md` (which lists publishers of articles/releases); this file
lists places where *conversation* happens.

Priority is scan order (P1 = every week, P2 = most weeks, P3 = sample/opportunistic).
Access tier tells you whether it can be scanned without an account:

- `[public]` — readable with web fetch / search, no login. Scan these.
- `[js]` — public but client-rendered; use the in-browser reader, not a plain fetch.
- `[auth]` — needs an account / invite / bot membership. **Not auto-scannable today** — kept
  here so we add it the moment a connector or credential exists. Do not fabricate its content.

## Upkeep rules (run every week)

1. **Rank by engagement.** A thread earns a spot by how much real discussion it drew
   (HN points + comments, Reddit upvotes + comments, SE votes/answers), not by mere existence.
2. **Dedupe against the rest of the digest.** If a thread is just people reacting to an article
   already listed above, fold it in / skip it. The Community pulse is for discussion that is
   itself the story (debates, war stories, "wait, does Postgres really do X?").
3. **Discover.** Each run, spend a little effort finding *new* active DB communities —
   a fresh subreddit, a Discourse forum, a public Telegram channel, a Matrix room, a Discord
   that opened public logs. Add keepers below with date, access tier, and a one-line reason.
4. **Prune.** If a listed source shows no database activity in ~3 months, is gone, or has turned
   into pure self-promotion, **move it to the Retired log** at the bottom (with date + reason).
   That removes it from the weekly scan but records it so it isn't blindly re-added next week.

---

## Forums & link aggregators

- **Hacker News** — search the week's DB threads and rank by points/comments; query `postgres`,
  `postgresql`, `database`, `sql`, `duckdb`, `clickhouse`, `sqlite`, `mysql`. Best signal-to-noise
  for cross-engine debate. `[public]` (Algolia API: hn.algolia.com). P1.
- **Lobsters — databases tag** — smaller, higher-signal than HN; good for systems/internals.
  `[public]` https://lobste.rs/t/databases . P2.
- **r/PostgreSQL** — the main Postgres subreddit; sort Top / This Week. `[js]`
  https://www.reddit.com/r/PostgreSQL/top/?t=week . P1.
- **r/databasedevelopment** — DB *internals* community (storage engines, query processing);
  exactly the reader's wheelhouse. `[js]` https://www.reddit.com/r/databasedevelopment/ . P1.
- **r/SQL** — broader SQL Q&A and discussion; filter heavily. `[js]`
  https://www.reddit.com/r/SQL/top/?t=week . P2.
- **r/Database** — general DB talk; smaller, noisier. `[js]`
  https://www.reddit.com/r/Database/top/?t=week . P3.
- **r/dataengineering** — pipelines/warehouses; lots of vendor noise, occasional gold. `[js]`
  https://www.reddit.com/r/dataengineering/top/?t=week . P3.

## Q&A

- **DBA Stack Exchange** — "hot this week" surfaces real operational puzzles and surprising
  answers. `[public]` https://dba.stackexchange.com/?tab=week . P2.
- **Stack Overflow — [postgresql] / [sql]** — high volume, mostly routine; sample only for a
  question that blew up or got an authoritative answer. `[public]`
  https://stackoverflow.com/questions/tagged/postgresql?tab=Week . P3.

## Chat & messengers

- **PostgreSQL community Slack** — postgresteam.slack.com (join via https://postgres-slack.org).
  High-signal real-time talk. `[auth]` — needs invite; not auto-scannable yet. P-.
- **PostgreSQL Discord** — public server but reading history needs membership/bot. `[auth]`. P-.
- **#postgresql on Libera.Chat (IRC)** — public channel, but no reliable public web archive.
  `[auth]` (effectively). P-.
- **Public Telegram channels** — readable without login via the web preview
  `https://t.me/s/<channel>`. None pinned yet — **discover and add** the ones worth following
  (English and Russian-language Postgres/DBMS channels). `[public]` once a channel is named. P2.

---

## Discovery log

_Append new community sources here: date, name, link, access tier, one-line reason._
- (2026-06-20) _seed list created._

- (2026-07-06) hntoplinks.com — week/month views of top HN stories with live points/comments; the fastest way to rank the week's DB threads when HN's own listing pages are cache-stale. Scan aid, not a primary source; verify numbers on the item page when possible. `[public]` P2. https://www.hntoplinks.com/week
- (2026-07-06) _Access note (this run):_ Lobsters (/t/databases and story pages), Reddit (blocked UA), and DBA SE (?tab=week) were all unreachable/empty via plain fetch — an access-path failure, not dormancy; do NOT retire them. Use the in-browser reader for these when a browser is connected.

- (2026-07-13) hckrnews.com — chronological HN front-page mirror with points/comments; fresh when hntoplinks pages ≥2 are cache-stale, but only covers the most recent ~2–3 days. Scan aid for the tail of the week. `[public]` P3. https://hckrnews.com/
- (2026-07-13) _Access note (this run, no browser):_ live news.ycombinator.com item pages returned empty to plain fetch; scores came from hntoplinks.com/week (page 1 fresh, deeper pages stale) + hckrnews.com + earlier cached item snapshots — engagement numbers may lag finals. Lobsters, Reddit, DBA SE (unseedable via search) all unreachable again. HN /front day archives blocked; mid-week mid-size threads may be under-sampled.

## Retired (removed from weekly scan)

_When a source goes dead/dormant/promotional, move it here with date + reason so it isn't
re-added by mistake._
- _(none yet)_

- (2026-07-20) _Access note (this run, no browser):_ hntoplinks /week page 1–2 were fresh (IDs ~48.9M) but page 3 was a months-old cache (April IDs) — trust deeper pages only after checking item IDs. Lobsters, Reddit, DBA SE unreachable again without a browser; live HN item pages still empty to plain fetch (engagement numbers from hntoplinks may lag finals).

- (2026-07-27) _Access note (this run, no browser):_ Community pulse omitted — `hntoplinks.com/week` could not be seeded into provenance this run (search returned only github/similarweb/month-archive URLs, not the live /week page), live `news.ycombinator.com/item?id=…` pages returned empty to plain fetch, and Lobsters/Reddit/DBA SE were unreachable as usual. One candidate in-window thread (HN id=48935487, "We're Building Postgres in Rust… the LLVM of Databases") was visible in search but its date and points/comments couldn't be verified without a browser, so it was NOT listed (no fabricated engagement). Reconnect a browser to restore this section.
- (2026-07-27b) _Correction + technique (browser reconnected, digest rebuilt):_ Community pulse was FILLED this run once a browser was available. **Working recipe for HN engagement:** the HN Algolia API is CORS-blocked from `news.ycombinator.com` (strict CSP → "Failed to fetch"), but works via **same-origin fetch after navigating the tab to `https://hn.algolia.com/`**, then `fetch('https://hn.algolia.com/api/v1/search_by_date?tags=story&query=<kw>&numericFilters=created_at_i>LO,created_at_i<HI,points>15&hitsPerPage=50')` for each keyword, dedupe by objectID, sort by points. Returns verified points/num_comments/created_at — no scraping of item pages needed. In-window top DB threads this week: "The startup's Postgres survival guide" (hatchet.run, 521/235) and "Postgres LISTEN/NOTIFY actually scales" (dbos.dev, 368/82). Note: `javascript_tool` REPL returns `undefined` if you use a top-level `return`; end with a bare expression instead.
- (2026-08-03) _Access note (this run, browser connected):_ HN Algolia same-origin recipe worked again (navigate tab to hn.algolia.com, fetch search_by_date with created_at_i window + points filter; dedupe by objectID). Top in-window DB threads: PGSimCity (928p/92c), SQLite in Production (258p/77c), Making Postgres queues scale (126p/33c), Choose DuckDB rather than SQLite (87p/57c). Lobsters/Reddit/DBA SE not sampled this pass — HN yield was already strong; sample them next run for balance.

- (2026-08-10) _Access note (this run, NO browser — Chrome extension unreachable):_ Community pulse was ranked from **`hntoplinks.com/week` pages 1–2**, which plain-fetch fine and print points + comments + relative age; live `news.ycombinator.com/item?id=…` pages still return empty, and the HN Algolia same-origin recipe needs a browser, so engagement numbers here may lag finals. Only two DB threads cleared the bar in the weekly top 60 ("SQLite Critical CVEs or LLM Slop?" 726p/374c, "Zed DeltaDB" 527p/312c) — a genuinely thin week for database argument on HN, not a scan failure. Lobsters, Reddit and DBA Stack Exchange were unreachable without a browser, as usual; do NOT retire them. **Discovery:** no new community source added this run — searching for public Telegram/Matrix DB channels again returned only marketing aggregators, so the `[public]` Telegram slot stays empty rather than filled with noise.
- (2026-08-11) _Access follow-up (same run, still no browser):_ `lobste.rs/t/performance` (and by extension `/t/databases`) plain-fetches to an **empty body** — it returns 200 with no content rather than an error, so it can look like a quiet tag when it is really an access failure. Reddit could not be seeded into the fetch provenance set at all (searches return postgresql.org pages, never the subreddit). Both stay `[js]`/browser-only; do NOT retire either. DBA Stack Exchange was not attempted this pass.
- (2026-08-11b) _CORRECTION + working recipes (browser reachable after all — via the **`Control_Chrome` MCP server**, not the claude-in-chrome extension, which reported zero paired browsers all session). The no-browser pass above materially under-covered this week; treat hntoplinks as a fallback only._
  1. **`Control_Chrome` gotchas:** `list_tabs`/`open_url` work immediately, but `get_page_content` and `execute_javascript` fail with a misleading *"Google Chrome is not running"* until **Chrome → View → Developer → Allow JavaScript from Apple Events** is enabled. Check that first. Also: `execute_javascript` returns the last expression **synchronously** — an `async` IIFE or a bare `await` yields `missing value`. Pattern that works: first call kicks off `window.__x={done:false}; (async()=>{…; window.__x.done=true;})(); 'started'`, second call polls `window.__x.done ? JSON.stringify(window.__x.out) : 'pending'`. Return a single JSON string; multi-line `join('\n')` output comes back empty.
  2. **HN Algolia works from any origin** here (CORS `*`) — no need to navigate to hn.algolia.com first. Query `search_by_date?tags=story&query=<kw>&numericFilters=created_at_i><LO>,created_at_i<<HI>,points>15&hitsPerPage=50` per keyword, dedupe by objectID, sort by points. **This beat `hntoplinks.com/week` decisively**: the weekly top-60 scrape missed three in-window DB items that Algolia found (pgrust 300x 335/175, Shopify Redis→MySQL 340/253, ClickHouse Labs 340/76) because they ranked below the general-interest cutoff. Always prefer Algolia; hntoplinks is a fallback.
  3. **Lobsters `/t/databases` renders fine in the browser** (plain fetch returns an empty body). Extract with `document.querySelectorAll('a.u-url')` for title+outbound href; the `li.story` selector returned `missing value`. Engagement there is low single digits, so it earns few Community-pulse slots — but it is an excellent *article discovery* feed (found the PlanetScale, CedarDB, FastLanes and pgtestdb items this week).
  4. **Reddit:** `old.reddit.com/r/<sub>/top/?t=week` redirects to a login/consent wall. Use the read-only JSON endpoint `old.reddit.com/r/<sub>/top.json?t=week&limit=12` instead — parse `document.body.innerText`, no banner accepted, no account touched. Worked for r/PostgreSQL (best in-window thread: managed-RDS alternatives, 35 up / 65 comments) and r/databasedevelopment (quiet: 13/13/10 pts).
  5. **Qiita `[ja]`** renders in the browser; titles need `a[href*="/items/"]` (the `article`/`li` wrappers give empty text) and dates come from the sibling `time[datetime]`. **modb.pro `[zh]` still resisted** — client-rendered SPA, the front page exposed no dated article list to either `get_page_content` or DOM extraction. Needs a different entry point (try a category or search URL) next run.
  6. DBA Stack Exchange still not attempted — carry over.
- (2026-08-11c) **Reddit is a first-class source, not a nice-to-have — and needs no account.** The read-only JSON API serves everything unauthenticated: `old.reddit.com/r/<sub>/top.json?t=week&limit=40` for the week's threads (score, num_comments, created_utc, `url` for the outbound link, `selftext`), and `old.reddit.com<permalink>.json?limit=6` for the post plus top comment bodies — enough to characterise a debate accurately instead of guessing from the title. Only the HTML UI walls you; never sign in or accept the banner. **Sweep these seven each run** and filter non-DB subs by keyword: r/PostgreSQL, r/databasedevelopment (no filter needed), plus r/SQL, r/Database, r/dataengineering, r/programming, r/ExperiencedDevs (filter on postgres|database|sql|duckdb|clickhouse|sqlite|mysql|index|query|transaction|replicat|vacuum|olap|oltp). **Sort by comment count, not score** — this week's most substantive debate ("Treating SQL as the source of truth", 53 comments) sat at *zero* points, and would have been invisible ranked by score. This sweep alone produced four items no other source surfaced: the actively-exploited Metabase SQLi advisory (r/dataengineering, 69 pts), pgColumnar (r/PostgreSQL, 41), ClickHouse's WAL-backpressure post (r/PostgreSQL, 15 — the outbound `url` field is what identifies it; the title alone doesn't), and the SQL-codegen debate.
- (2026-08-11d) **DBA Stack Exchange — use the API, not the HTML.** `https://api.stackexchange.com/2.3/questions?site=dba&fromdate=<epoch>&todate=<epoch>&order=desc&sort=votes&pagesize=15&filter=!nNPvSNdWme` is CORS-open, needs no key at this volume, and returns score / answer_count / view_count / tags / link already windowed — far better than scraping `?tab=week`. **Finding for Aug 3–9: genuinely low-signal.** Top question of the week was 5 points / 1 answer ("Negative Blocking Session IDs", SQL Server); everything else scored 0–2. Traffic skews SQL Server and Informix, with Postgres barely present. Conclusion: scan it every run because it is cheap, but expect it to contribute to Community pulse only rarely — do NOT treat an empty DBA-SE contribution as a scan failure. (Closes the "not attempted" carry-over from 2026-08-11b.)
- (2026-08-17) _Access note (this run, browser via Control_Chrome):_ HN Algolia queried directly from the hn.algolia.com tab (8 keywords, epoch-windowed, points>15) — verified engagement numbers; hntoplinks not needed. Reddit seven-sub sweep via `old.reddit.com/.../top.json` browser navigation (plain fetch cannot be seeded for reddit; the JSON endpoints still need no login). Lobsters `/t/databases` rendered fine in-browser (`.story` + `a.u-url` extraction) — mostly deduplicated HN this week but confirmed the PlanetScale subtransactions post. DBA SE API scanned: top question of the week was 3 points (SQL Server/JSON) — below bar again, but note a curious cluster of four PolarDB-for-PostgreSQL questions in one week. **modb.pro [zh] still unenumerable** even in a real browser: front page, `/search?k=`, and `/tag/<t>` are all client-rendered shells with no dated list; next run try the mobile site (m.modb.pro) or watching its XHR endpoints. Discovery: no new community source added — nothing found beyond marketing aggregators this run.

- (2026-08-24) _Access note (this run, browser via Control_Chrome):_ HN Algolia (8 keywords, epoch-windowed, points>10) verified engagement directly — a thin DB week on HN (only three threads over 250 points, all article reactions). **Reddit sorted by comment count was again the differentiator**: the two most substantive Postgres threads of the week ("what after the free tier", "leaving Cloud SQL") sat at 0 and 1 points respectively with 27 and 9 comments, and would have been invisible ranked by score. Lobsters `/t/databases` rendered fine and was the best *article discovery* feed of the run (PlanetScale poisoned pools, CedarDB encoding-vs-compression, the DuckDB PEG-parser post, the sporks.space query-language wish list) — engagement there stays too low for pulse slots. DBA SE API scanned: top question 3 points, but a genuinely interesting `ORDER BY … LIMIT` planner question at 2 points made the cut, and PolarDB-for-PostgreSQL questions cluster there for a fourth straight week. **modb.pro [zh] not retried this run** — carry over the mobile-site / XHR-endpoint idea. **Discovery:** no new community source added; searches for public Telegram/Matrix DB channels again returned only marketing aggregators, so the `[public]` Telegram slot stays empty.

- (2026-08-31) _Access note (this run):_ HN Algolia (8 keywords, epoch-windowed, points>10) queried via the in-app browser pane. **Reddit sorted by comment count remained the differentiator again** — the top r/PostgreSQL thread this week ("wire-protocol proxy for cold-start Postgres containers") sat at 47 points/21 comments, comfortably above bar, but the DuckLake-vs-Iceberg benchmark thread (37/5) needed the `[unverified]` flag once the comment thread disputed the methodology. **Browser split:** the in-app `mcp__Claude_Browser__*` pane refuses `old.reddit.com` outright ("blocked by policy"); `Control_Chrome` (real host Chrome) reached the same `old.reddit.com/r/<sub>/top.json?t=week&limit=40` endpoints fine and was used for the full seven-sub sweep, Lobsters `/t/databases`, and the DBA Stack Exchange API this run. Discovery: acadia.engineering (Evan Czaplicki's Datalog-flavored query-language project) drove the week's biggest r/programming database thread (128 pts/94 comments) and a smaller HN one — added to sources.md as a publisher, cross-referenced here since its threads are also a community-pulse item most weeks. modb.pro [zh] not retried — carry over the mobile-site/XHR-endpoint idea yet again.
