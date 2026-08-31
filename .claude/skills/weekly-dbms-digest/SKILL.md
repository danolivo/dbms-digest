---
name: weekly-dbms-digest
description: Build a weekly, ad-free digest of PostgreSQL and broader DBMS news, research, and cutting-edge tech — including new techniques and inventions in commercial engines (SQL Server, Oracle, MySQL, etc.) and real-world migration experience reports. Use this skill whenever the user asks for the "weekly digest", "Postgres digest", "DBMS digest", "database news roundup", "what happened in databases this week", or when a scheduled task asks to generate the weekly database digest. The skill curates high-signal sources, finds items published in the last 7 days, ruthlessly filters out advertising / vendor promotion / marketing fluff, fact-checks claims, and emits a terse headline + one-line list of links. It also discovers and records new emerging sources each run so the source list stays fresh.
---

# Weekly DBMS Digest

Produce a short, high-signal weekly digest of what actually happened in the PostgreSQL and wider database world: new technologies, real engineering, cutting-edge inventions, and research. This explicitly includes new techniques and inventions in **commercial engines** (SQL Server, Oracle, MySQL, DB2, etc.) and **real-world migration experience** reports — the reader cares about what other databases are doing and what actually happens when people move data between them. The reader is a Postgres hacker who is allergic to marketing. The single most important job of this skill is to **separate signal from sales**: surface genuine technical/research content and discard (or clearly flag) advertisement, company promotion, and marketing material.

The output is deliberately terse: each item is a **headline + one line** with a link. The reader wants to scan 15–30 items in two minutes and click into the 3–4 that matter.

## Workflow

Follow these steps in order. Don't skip the filtering and fact-check steps — they are the whole point.

### 0. Fetching technique (read this first — it unblocks everything below)

`web_fetch` will only retrieve a URL that has already appeared **in a prior search
result or a previously fetched page** ("provenance"). A cold `web_fetch` of a feed or
archive URL you just typed will fail with *"URL not in provenance set"*. This is the single
biggest reason past runs skipped the mailing lists and the non-English sources. Defeat it
deliberately, every run:

1. **Seed with a search.** Run a `WebSearch` whose results contain the index/feed/page you
   want (e.g. search `mail-archive.com pgsql-hackers <topic>` or the site name). The result
   URLs are now fetchable.
2. **Chain through fetched pages.** Every link **on a page you fetched** is itself now
   fetchable. So fetch an index page, then fetch the items it links to, then their
   Previous/Next/thread links — you can walk an entire week this way without another search.
3. **Feeds the same way.** To read an RSS/Atom feed whose URL won't fetch cold, first fetch
   (or search) the site's HTML page; its `<link rel=alternate>`/feed URL becomes fetchable.
4. **JS-heavy or empty results → browser.** If a fetch returns an empty shell or a loading
   page (client-rendered sites: modb.pro, Reddit `.rss`, Qiita, Lobsters tag feed), switch to
   the Claude-in-Chrome browser tools to render it. Never `curl`/script around a failed fetch.
5. **If a page is too large**, it is saved to a file path the tool reports — but that path is
   on the host, not in the sandbox mount, so you usually can't open it. Prefer fetching a
   narrower URL (a single thread, a single month) over a giant index.

### 1. Establish the time window

The digest covers the **last 7 days** by default (or the span since the previous digest if the user gives one). Compute the date range with `date` so you don't rely on a guessed "today". Items published outside the window are excluded, even if interesting — note them only if genuinely seminal.

### 2. Gather candidate items from known sources

Read `references/sources.md` for the curated source list, grouped into Postgres, broad DBMS, research venues, and aggregators/newsletters. Work through the high-priority sources first. Prefer aggregators (Planet PostgreSQL, DB Weekly) to fan out quickly, then go direct to primary blogs for anything promising.

**Feed-first ingestion (all languages).** The fastest, most reliable, language-agnostic scan is the curated feed list in `references/feeds.opml` — an OPML list of RSS/Atom feeds. Each run, fetch every feed and keep items whose publish date falls in the window; RSS/Atom is plain XML, so a normal fetch works — no browser, no language barrier. Three cases need the **Claude-in-Chrome** browser instead: feeds blocklisted for plain fetch (Reddit's `.rss` is — confirmed), live feeds that come back empty/unparseable through plain fetch (Lobsters' tag feed and Cybertec's WordPress feed do — they're fine in a real reader), and sources with no feed yet (several Chinese aggregators). Maintain `feeds.opml` like the other source lists: add a feed when you find/confirm one (discover the URL in the browser if the site doesn't advertise it), and drop a feed only when it's genuinely dead (404 / gone) — not when plain fetch merely returns empty (read those via the browser instead). It's also importable into any reader.

Use web search and page fetches to collect: title, URL, author/source, publish date, and enough of the body to judge it. Cast a wide net here — filtering happens next.

**Scan non-English sources too (NON-SKIPPABLE — pull several languages every run).** The Chinese, Japanese, Russian, French and German DB ecosystems are active weekly; defaulting the International section to "Russian only" or omitting it means you under-scanned, not that nobody published. Each run, actively query **at least ru + zh + ja** plus one of fr/de. Work the multilingual set in `references/sources.md` (Russian, Chinese, French, German, Japanese). Search in the **native language** — the best regional engineering write-ups never surface in English search, so query with native terms (e.g. база данных, 数据库, base de données) alongside `PostgreSQL`. Apply the same anti-marketing and fact-check bar, and be careful not to let a machine translation distort a technical claim — verify numbers/behaviour against the original or a primary source. Present these per the non-English formatting rule below.

**Tooling for non-English / JS-heavy sources.** Plain page fetches only see raw HTML, so client-rendered or region-specific sites (Chinese aggregators like modb.pro, PolarDB / Alibaba Cloud, PingCAP — also Reddit and Qiita) often return stale or empty content. In order of preference: (1) use each source's **native RSS/Atom feed** (listed in `references/sources.md`) — feeds are dated, language-native, and fetch cleanly; (2) when there's no usable feed, **render the page with the Claude-in-Chrome browser tools** rather than a plain fetch; (3) treat web search as English/US-biased — use it to confirm, not to discover, non-English items. The Chinese ecosystem in particular publishes heavily and is mostly invisible to English search, so lean on its feeds and the browser.

### 3. Scan PostgreSQL mailing lists

Scan the four key lists for the current time window. Use the PostgreSQL list archives at `https://www.postgresql.org/list/<listname>/` (monthly view) or web-search `site:postgresql.org/message-id` with topic keywords to pull specific threads.

**Lists to scan (in priority order):**
- `pgsql-hackers` — new feature proposals, patch reviews, design debates, committer decisions
- `pgsql-bugs` — confirmed bugs and surprising regressions; ignore "user error" threads
- `pgsql-performance` — unexpected slowdowns, benchmark surprises, planner misbehaviour reports
- `pgsql-general` — only surface items where a core developer or committer gave a notable/surprising answer; skip routine user questions

**What qualifies** (be selective — list traffic is high; signal is rare):

*New threads worth surfacing:*
- A new feature or design proposal with a concrete patch or detailed spec
- A confirmed bug or regression with a reproducible test case or bisected commit
- A benchmark result or performance finding that is surprising relative to prior behaviour
- A design debate where the outcome (accept / reject / defer) is itself informative
- A security or data-loss risk being actively discussed

*Changes in ongoing threads worth surfacing:*
- A thread that was stalled or controversial and just reached a resolution (committed, rejected, redesigned)
- A significant objection raised against a previously-accepted approach
- New data (benchmark, counter-example, real-world report) that materially shifts the discussion
- A committer expressing a strong opinion that narrows or redirects the design space

**What to skip:**
- "How do I do X?" threads without a core-developer surprise in the answer
- Patch submissions still in early review with no substantive feedback yet
- Threading noise: replies that just say "+1" or "thanks"
- Build/packaging questions unless a portability bug is confirmed

**How to scan (PROVEN RECIPE — do not skip the lists, ever).** The mailing lists are
high-signal and almost always have in-window activity; an empty mailing-list section means you
didn't look, not that the list was quiet. Use whichever of these works this run:

- **Official archive in a BROWSER — try this FIRST; it is the highest-yield path by far.**
  `https://www.postgresql.org/list/<listname>/<YYYY-MM>/` renders fully in a real browser and
  returns an empty shell to plain `web_fetch` — do not mistake the empty fetch for a dead source.
  The page carries a "Jump to day" strip of `/list/<listname>/since/YYYYMMDD0000/` links; from
  that tab, same-origin `fetch()` each day in the window and parse with `DOMParser`.
  **Parsing trap:** the subject anchor lives in `th[scope="row"]`, *not* a `td` — select
  `th a[href*="/message-id/"]` for subject+href, then `td[0]` = author, `td[1]` = time; a trailing
  📎 means an attachment (usually a patch). Each `since/` page spans several days, so parse under
  the `<h2>Mon. N, YYYY</h2>` headers and dedupe. New threads = subjects not starting with `Re:`.
  Then read the ones that matter via `https://www.postgresql.org/message-id/flat/<id>` (whole
  thread) or `/message-id/<id>` (single message, body in `.message-content`) — characterise a
  thread from its text, never from its subject alone. Works identically for `pgsql-hackers`,
  `pgsql-bugs`, `pgsql-performance` and `pgsql-general`. A typical -hackers week is ~600 messages
  and ~90 new threads; if you got fewer, your parser is wrong, not the week.
- **mail-archive.com (fallback; good for full text + dates, and the only fresh source for
  `pgsql-committers`).** Seed once with
  `WebSearch` for `mail-archive.com pgsql-hackers <topic>`, then fetch
  `http://www.mail-archive.com/pgsql-hackers@lists.postgresql.org/maillist.html` (and the
  `mail2.html`, `mail3.html`… "Earlier messages" pages) for a date-ordered list. Each message
  is `…/msgNNNNNN.html`; **numbers are sequential, higher = newer**, and every page prints a
  real date (`Sun, 21 Jun 2026 …`) plus Previous/Next and a full thread index you can chain
  through. Walk back from the newest message until you cross the Monday boundary.
- **Official archive.** `https://www.postgresql.org/list/` links to each list
  (`/list/pgsql-hackers/`, `/list/pgsql-bugs/`, `/list/pgsql-performance/`, `/list/pgsql-general/`)
  and its monthly view `…/2026/06/`; `https://www.postgresql.org/message-id/flat/<id>` renders a
  whole thread. Reach these by chaining from the `/list/` page (fetch it first to put the links
  in provenance).
- **Cross-check** any surprising claim against the git commit or CommitFest entry before
  including it. Aim to scan the subject lines of the top 20–30 threads per list, pick the few
  that meet the "what qualifies" bar, and link the thread root.

**Format for mailing list items** (goes in the `## PostgreSQL mailing lists` section):
```
- **[hackers] [<Thread subject>](archive URL)** — <one line: what was proposed/found/decided and why it matters>. *(<proposer/committer>)* `[patch posted]`
- **[bugs] [<Thread subject>](archive URL)** — <one line: confirmed bug / regression / data-loss risk>. *(<reporter>)* `[open]`
```
Tag with the list name in brackets and make the **thread subject the link** — to the thread root in the archive, not a specific reply (unless a specific reply is the event). Add the key person (proposer / committer / reporter) in italics after the line, e.g. `*(Jeff Davis · pgsql-hackers)*`. Append `[committed]`, `[rejected]`, `[patch posted]`, `[needs review]`, or `[open]` to show where things stand.

### 3b. Open CommitFest balance (PostgreSQL development pulse)

Track the open CommitFest every run — it is the clearest single signal of where core
development is heading, and it must not be skipped. **Do NOT fetch the full CF list page**
(`/<n>/` is ~180 KB, usually overflows the fetch limit, and has no totals anyway). Instead:

1. Fetch `https://commitfest.postgresql.org/` to find the **open** CF and its number
   (e.g. *Open: PG20-1* → `https://commitfest.postgresql.org/59/`).
2. Fetch the **per-CF activity log** `https://commitfest.postgresql.org/<n>/activity/`. It is
   small, dated, and current — note that the *global* `/activity/` page is often served stale
   from cache, but the **per-CF** one is fresh. Each row is `time · user · patch · activity`.
3. From the rows inside this digest's Mon–Sun window, compute the week's **flow**:
   `Created patch record` = new entries; `Closed … Committed/Withdrawn/Rejected/Returned with
   feedback` = entries leaving; also note `New status: Ready for Committer` promotions.
   Net balance = created − closed.
4. **Persist a snapshot** to `references/commitfest-state.json` (one object per ISO week:
   `{week, cf, captured_at, created:[{id,title,by}], closed:[{id,title,status}], net}`).
   Each run, diff against the previous week's object so the digest can state how the balance
   moved week over week. Commit this file with the digest.
5. Pick the **single most interesting new entry** and summarise its gist in one line — read its
   linked mail thread if the title isn't self-explanatory. Prefer internals features
   (planner, storage, replication, executor) over trivial doc/typo patches.

The first run has no prior snapshot, so report the week's flow and say the week-over-week
baseline starts now — never invent a previous-week total. If the activity page only covers part
of the window, say so rather than implying a complete count.

### 4. Scan community discussion — the “Community pulse”

Read `references/community-sources.md` and scan the **scannable** community sources (the `[public]` / `[js]` ones) for the time window: forums and link aggregators (Hacker News, Lobsters), the database subreddits, Q&A hot lists (DBA Stack Exchange), and any pinned public Telegram channels. The goal is **what people actually argued about this week**, ranked by real engagement (HN points + comments, Reddit upvotes + comments, SE votes/answers) — not by mere existence.

Pick the 3–8 threads with the most substantive discussion. **Dedupe against the rest of the digest**: if a thread is just reactions to an article already listed above, fold it in or skip it — the Community pulse is for discussion that is itself the story (design debates, war stories, “wait, does Postgres really do X?”, surprising benchmarks people are passing around). Apply the same anti-marketing filter, and link to the thread itself.

Follow `community-sources.md`'s upkeep rules every run: **discover** new active DB communities (a fresh subreddit, a Discourse forum, a public Telegram/Matrix channel) and append keepers to its Discovery log; **prune** any listed source that's been silent for ~3 months, is gone, or has turned promotional by moving it to that file's Retired log (with date + reason) so it leaves the weekly scan but isn't blindly re-added. `[auth]` sources (the community Slack / Discord / IRC) stay listed but are **not** scanned until a connector or credential exists — never fabricate their content.

### 5. Conferences — open CFPs and upcoming events

Two date-windowed sections, each tied to **this** week so the same item never appears in two digests.

**Call for papers** — list a CFP **only in the digest for the week its call opened** (the "CfP is now open" announcement falls inside this digest's 7-day window). One announcement → one digest; never list a CFP that opened in an earlier week or that is merely "still open". Cover both buckets, but only when the call was announced in-window:
- **PostgreSQL community events** — conferences, PGDays, meetups (PGConf.dev/EU/NYC/India, Nordic PGDay, PGDay Paris/Boston/UK/Lowlands/Israel, FOSDEM PGDay, Prague PostgreSQL Developer Day, Swiss PGDay, …). Use the PostgreSQL **news archive** ("…CfP is now open" posts carry a date), the Conferences & CFP trackers in `references/sources.md`, and dev.events/postgres.
- **Applied & research DB-systems venues close to Postgres** — VLDB, SIGMOD, CIDR, ICDE, DEBS, USENIX ATC/OSDI, P99 CONF, HYTRADBOI (venue CFP pages, WikiCFP).
Give the conference, location + dates, the **CFP deadline**, and the link; tag *(community)* or *(research)*. If no CFP opened this week, omit the section.

**Upcoming events** — a one-month heads-up with **no repeats**: list a conference/PGDay/meetup exactly once, in the digest for the week during which it **enters the 30-day horizon** — i.e. its start date is **24–30 days after the end (Sunday) of this digest's week** (an event more than 30 days out waits for a later digest; one already ≤23 days out was listed last week). For each qualifying event, open the program and pick the **1–3 talks most interesting to an internals developer** — ideas you could implement or probe in your own engine/product (wire protocol, planner/optimizer, storage, MVCC, replication, memory, concurrency, indexing), **not** generic intro/ops talks; give speaker + a one-line "why it matters". If the program isn't posted yet, list the event and say so. If nothing enters the horizon this week, omit the section. Discover events via the Conferences & CFP trackers in `references/sources.md`, the PostgreSQL events page, and dev.events.

### 6. Discover emerging sources (self-update)

Each run, spend a little effort looking for **new, high-quality sources** that aren't yet in `references/sources.md`: a new independent engineering blog, a fresh research group page, a newly active newsletter, a conference that just posted proceedings. Good signals are: cited by sources you already trust, written by known contributors, deep technical content with no sales pitch.

When you find a keeper, **append it to `references/sources.md`** under the right section with a one-line note on why it's worth watching, **and give it an outlet class** (`[solo]`/`[org]`/`[pipe]` — see the "Outlet key" note near the top of that file). This is how the skill stays current instead of going stale. Conversely, if a listed source has gone dormant or turned into pure marketing, mark it accordingly.

**Reconcile `references/feeds.opml` against `references/sources.md`, every run, at the end of this step.** The two lists drift apart silently otherwise — feeds.opml only tracks confirmed-fetchable feed URLs while sources.md is the full outlet list, so they will never be identical, but a source that's been P1/P2 for months with no feed entry and no noted reason ("no feed exists," "renders JS, browser-only") is a gap worth closing. Spend a minute: skim sources.md for a P1/P2 outlet missing from feeds.opml, try to find its feed, and add it (or add a one-line note in feeds.opml explaining why it can't have one). This is a cheap check, not a full feed-discovery pass.

### 7. Filter out marketing, ads, and promotion

This is the core value of the digest. **Exclude** an item (or flag it clearly if it's borderline but still has real content) when it shows the hallmarks of marketing rather than engineering:

- It's primarily announcing a product, pricing, funding round, partnership, award, or "we're now GA" with little technical substance.
- It's a vendor case study whose real purpose is the logo and the CTA, not the method.
- Superlatives without numbers: "blazing-fast", "next-gen", "revolutionary", "game-changing", "enterprise-grade" with nothing measured.
- It ends in a demo booking, free-trial, or "talk to sales" call to action and the body was just a runway to it.
- Reposted press release / sponsored content / listicle SEO bait ("Top 15 databases for 2026").

**Keep** content that teaches or proves something: benchmarks with methodology, internals deep-dives, postmortems, release notes that explain *what changed and why*, research papers, protocol/design discussions, reproducible experiments — even when published on a vendor's blog. A vendor engineering blog post can be excellent; judge the substance, not the domain. When in doubt, ask: "If I strip the company name, is there still something I learned?" If no, cut it.

**Feature-explainer rule (authority gate).** A lot of posts just describe a new or existing feature without adding a new use case, a problem found in the wild, a benchmark, or a non-obvious gotcha. These "here's how feature X works" walkthroughs are only worth including when written by someone with first-hand authority over that feature — its **author, committer, or reviewer** (for Postgres, check the commit / CommitFest / release-note credits; for other engines, the engineer who built or shipped it). If a generic feature explainer is written by someone *without* that direct involvement, skip it — it's usually a rehash. The exception is the moment a feature first ships (a release/beta announcement), which is news regardless of author. When you do include an authority-written feature post, you may note the author's role, e.g. `[by committer]`.

**Commercial-engine techniques.** Actively look for genuinely new techniques and inventions in SQL Server, Oracle, MySQL, DB2, and similar — new optimizer/storage/replication capabilities, internals write-ups, and engineering deep-dives. Apply the same anti-marketing filter: a real technique or measured result, not a "what's new in version N" sales sheet.

**Release posts get a changes summary.** When an item is the release of an extension or utility (e.g. "pg_kpart 1.0", "powa-archivist 5.1.2", "pgBackRest 2.x"), don't just say "new release" — read the changelog/release notes and summarise *what actually changed*: the headline new features, notable fixes, breaking changes, and the minimum/target server version. This is the one place to relax the strict one-line limit — a release item may use a short sub-bullet list of the key changes when that's clearer. Skip pure version-bump posts with no meaningful changes, and still drop release posts whose "changes" are entirely marketing.

**Migration experience.** Actively look for real-world migration experience reports — moving to/from Postgres, Oracle→Postgres, MySQL→Postgres, cross-cloud, version upgrades at scale — where the author shares what actually happened (pitfalls, downtime, data discrepancies, tooling, rollback). These are high-value; prioritise them. Generic "why you should migrate to our product" posts are marketing — cut them.

### 7b. Record the ledger

This step exists to answer one question over a quarter: which outlets systematically give nothing back, so the weekly scan can stop wasting time on them. It does **not** change what gets filtered — steps 7 and 8 above are untouched — it only records, per candidate, the verdict those steps already reached.

**What's a candidate.** A candidate is anything that reached this point: it fell inside the Mon–Sun window and is on-topic for DBMS, so it survived the date and relevance triage that happens *before* filtering. Do not log items dropped purely for being out-of-window or off-domain before you ever considered them — that would make the denominator drift run to run. A candidate is logged exactly once, whether step 7/8 kept it (→ published) or cut it (→ dropped), across all five funnel categories: PostgreSQL mailing lists, blogs (the `## PostgreSQL`, `## Wider DBMS`, `## Commercial engines`, `## Migration experience` sections), community pulse, research, and international.

**Outlet key.** Normalize per the "Outlet key" rule in `references/sources.md`: lower-case, no `www.`, no trailing slash, no `utm-*`; domain, or domain+path for a shared platform (`dev.to/franckpachot`, `habr.com/ru/companies/postgrespro`). The same post reached via an aggregator and via the author's own site is one candidate keyed to the personal site.

**Outlet class.** Look up `[solo]`/`[org]`/`[pipe]` in `references/sources.md`. Mailing lists and community-pulse platforms (pgsql-hackers, pgsql-committers, Hacker News, Lobsters, Reddit, DBA Stack Exchange, a Habr *hub* scanned as a whole) are `pipe` by definition — don't look those up, just tag them `pipe`. Every entry in the categorized sections of sources.md carries a class as of 2026-08-31; if you land a candidate from an outlet that still has none (it's sitting unresolved in the "New sources added" log, or you just found it this run), resolve the class in sources.md before writing the ledger row — there is no default-to-`org` fallback here, since a fallback that always guesses the same way is worse than a five-second lookup. A source tagged `[no-ledger]` in sources.md (e.g. a composite entry that bundles several real outlets under one line) never gets a ledger row of its own — attribute the candidate to the real domain of the post instead.

**Two files, one per candidate row, written together:**

- `references/ledger.tsv` — git-ignored (alongside `exclude.md`), full detail, local diagnostic only:
  `run_date  url  outlet  outlet_class  verdict  reason_code`
  (`verdict` is `published` or `dropped`.) This is what lets a future run tell "this outlet gives nothing" apart from "the pipeline missed it."
- `references/yield-stats.tsv` — **committed with the digest**, the aggregate:
  `run_date  outlet  outlet_class  candidates  published`
  No URLs, no author names, no reason codes — just two counts per outlet per run; the drop count is `candidates - published`, not stored separately. This file carries no judgment calls, so it's fine to publish.

Append rows to both files as you work through steps 7–8, in the same run — don't reconstruct them afterward from memory.

**Reason codes (`ledger.tsv` only — closed list, edit SKILL.md to add one, never invent one mid-run):**

| Code | Meaning |
|---|---|
| `PRODUCT` | Product/pricing/funding/GA announcement, no technical substance |
| `CASE` | Vendor case study written for the logo and the CTA |
| `HYPE` | Superlatives with no numbers behind them |
| `SEO` | Listicle, press-release reprint, or SEO bait |
| `REHASH` | Feature explainer with no first-hand authority (the step 7 authority gate) |
| `DUPE` | Same story already in this issue |
| `OFFTOPIC` | Keyword match, not actually about DBMS |
| `THIN` | On-topic but below the bar — no method, no finding |
| `UNVERIF` | Key claim couldn't be substantiated (step 8) |

`DUPE` and `OFFTOPIC` are reasons on *our* side (dedup, query precision), not the outlet's — that distinction is exactly what the quarterly review below uses to avoid punishing a source for our own noise.

### 8. Fact-check before including

For each surviving item, do a quick sanity pass: does the headline claim match the body? Are benchmark claims accompanied by setup details (hardware, dataset, versions)? Is a "Postgres now does X" claim actually in a release/commit, or just speculation? Cross-check surprising claims against a second source (commit, mailing-list thread, the actual paper). If a claim can't be substantiated, either drop the item or append a short `[unverified]` note so the reader knows.

### 9. Write the digest

Use the exact format below. Keep each line to roughly one sentence — the value is in being scannable. Order items by importance (most significant first), lightly grouped by theme. Aim for ~10–25 items; quality over quantity. If a slow week yields little, a short honest digest beats padding.

## Output format

```
# DBMS Weekly — <YYYY-MM-DD> (week of <start>–<end>)

## PostgreSQL
- **[<Headline>](URL)** — <one-line why-it-matters>. *(<Author> · <source>)*
- ...

## PostgreSQL mailing lists
- **[hackers] [<Thread subject>](archive URL)** — <one line: what was proposed/found/decided>. *(<proposer>)* `[patch posted]`
- **[bugs] [<Thread subject>](archive URL)** — <one line: confirmed bug or regression>. *(<reporter>)* `[open]`
- ...

## CommitFest (open: <CF name>)
- **Balance (<window>):** <N> new · <M> closed (<x> committed / <y> withdrawn) → net <±k>. *(vs last week: <±delta>, or “baseline — tracking starts this week”)*
- **New this week:** **[<standout title>](CF URL)** *(author)* — <one-line gist>; also <title> (#id), <title> (#id).
- **Closed:** <title> (#id, committed), <title> (#id, withdrawn).

## Community pulse
- **[<What people were arguing about>](thread URL)** — <one line on the debate / war story / surprise and where it landed>. *(<platform> · <N pts / comments>)*
- ...

## Wider DBMS & distributed data
- **[<Headline>](URL)** — <one line>. *(<Author> · <source>)*
- ...

## Commercial engines (SQL Server, Oracle, MySQL, …)
- **[<Headline>](URL)** — <one line on the new technique/invention>. *(<Author> · <source>)*
- ...

## Migration experience
- **[<Headline>](URL)** — <one line on what actually happened>. *(<Author> · <source>)*
- ...

## Research & cutting edge
- **[<Headline>](URL)** — <one line>. *(<authors / venue>)* _[paper]_
- ...

## International (non-English sources)
- **[<English headline>](URL)** — <one-liner>. *(<Author> · <source>)* [ru] _(orig: <original title>)_
- ...

## Call for papers
- **[<Conference> — <location>, <dates>](CFP URL)** — CFP closes <deadline>. *(community)*
- ...

## Upcoming events
- **[<Event> — <location>, <dates>](schedule URL)** — <one line>. Internals picks:
    - **<Talk title>** (<speaker>) — <why it matters to an internals developer>.
    - ...

## New sources added this week
- **[<source name>](URL)** — <why it's worth following>. *(<author>)*

---

_<N> items · yield — mailing lists: <messages in window> → <shortlist> → <published> · blogs: <posts in window> → <shortlist> → <published> · community: <threads viewed> → <shortlist> → <published> · research: <preprints in window> → <shortlist> → <published> · international: ru <a>→<b>→<c>, zh <a>→<b>→<c>, fr …, ja … (only the languages actually worked this run)_
```

Notes on the format:
- **The headline is the link** (`**[Headline](URL)**`) — one big tap target, ideal on a phone; do not add a trailing `[link]`. The one-liner says *why a Postgres hacker should care*, not just what it is.
- **End each item with the author/source in italics**, e.g. `*(Christophe Pettus · thebuild.com)*`. Include the author's name when it isn't already in the one-liner; otherwise just the source/site (or venue, for papers). On a phone this lets the reader triage before tapping.
- Append `[paper]`, `[unverified]`, `[by committer]`, `[vendor blog — substantive]`, or a language tag (`[ru]` `[zh]` `[fr]` `[de]` `[ja]`) only when useful.
- **Non-English items go in their own `## International` section** (don't scatter them across the topical sections). Each gets an English headline + one-liner, a language tag (`[ru]` `[zh]` `[fr]` `[de]` `[ja]`), and the original title in italics in parentheses — e.g. `- **[Inside PolarDB's shared-storage buffer pool](URL)** — how it decouples buffer management from local disk. *(Alibaba Cloud · developer.aliyun.com)* [zh] _(orig: …)_`. Verify technical claims against the original, not just the translation. **Actively pull several languages each run (ru, zh, fr, de, ja)** — don't let the section default to Russian. For Chinese, `modb.pro` renders via the browser (`cn.pingcap.com` times out on idle); it's PR-heavy, so mine the research / internals items (OceanBase, TiDB, PolarDB) and drop vendor PR.
- **Release items** (extension/utility releases) may break the one-line rule: give a headline line plus an optional short indented sub-list of the key changes (new features, notable fixes, breaking changes, target server version). Example:
  ```
  - **[pg_kpart 1.0](URL)** — new index-time guard against full-partition scans. *(<author> · <source>)*
      - rejects queries that scan all partitions without the partition key
      - PostgreSQL 18+
  ```
- **Community pulse items** link to the discussion thread and tag the platform plus a rough engagement signal, e.g. `*(Hacker News · 240 pts, 180 comments)*` or `*(r/PostgreSQL · 95 upvotes)*`. Keep to the 3–8 most-discussed threads, deduped against the rest of the digest.
- **Call-for-papers items** appear only in the digest for the week the CFP **opened** (announcement in-window) — never repeated across weeks; tagged *(community)* or *(research)*.
- **Upcoming-events items** appear once, ~a month ahead — the event starts 24–30 days after this digest's week ends — then a short sub-list of 1–3 internals-relevant talks (speaker + why-it-matters), or a note that the program is TBA.
- **Blank line before every list.** A bullet list must be preceded by a blank line (CommonMark). If a section opens with an intro sentence (e.g. the Call-for-papers "open as of …" line), leave a blank line before the first `-`, or the whole block renders as one paragraph instead of a list.
- **The stats line is a funnel, not a single filtered-count.** Give each of the five candidate categories — mailing lists, blogs, community, research, international — its own three numbers: how many turned up in the window, how many made the shortlist (survived date/relevance triage — the ledger's "candidates"), how many actually ran. International breaks the same three numbers out per language, listing only the languages this run actually worked; omit a category's numbers if that category was skipped entirely rather than printing zeros that imply it was scanned. These numbers must match what you wrote to `references/yield-stats.tsv` this run (step 7b) — they're the same counts, just re-summed by category instead of by outlet.
- **Never name what was filtered — in the issue.** Never list the specific blogs, companies, people, or products you excluded — no "incl. X, Y …" enumerations and no "excluded: …" notes anywhere in a digest, and therefore nowhere on the published site (`build_feed.py` only reads `digests/*.md`). (Listing the sources you *scanned* is fine — that's coverage stats.) This is item-level privacy, and it's absolute. Outlet-level yield is a different thing and is tracked openly in the repo: `references/yield-stats.tsv` is committed, and a source in `references/sources.md` already carries a public verdict once it's been reviewed — `[low-yield]`, `[dormant]` — the same way DB Weekly already carries `[dormant]` there. Publisher-level accounting is public; which specific piece got cut, and why, stays local to `references/ledger.tsv`.
- **Owner privacy.** Never include a post **authored by** the digest's owner, and never print the owner's name or personal handles anywhere in the digest. The owner's names/handles live in `references/exclude.md` (git-ignored); skip anything authored by or naming them. Posts about the owner's employer written by *other* people are fine.
- **Skip empty sections silently.** Omit any section that has no items — do NOT write "nothing this week", "no items found", or an apology/explanation. A missing section just means nothing qualified; the reader infers that. Never add filler narration about gaps.
- If delivering to Telegram or another plain-text channel later, the same content works; just drop the Markdown headers to bullet groups if the target doesn't render Markdown.

## Example items

**Good (keep):**
`- **[Skip scan lands in Postgres 18](URL)** — btree now skips leading index columns, killing a class of "add a redundant index" workarounds; commit shows up to 20x on low-cardinality prefixes. *(pganalyze.com)*`

`- **[hackers] [Rethink hash join memory accounting](URL)** — Melanie Plageman proposes replacing the current executor-side batch-spill heuristic with a planner-visible cost model; thread has substantive back-and-forth on the right abstraction boundary. *(Melanie Plageman · pgsql-hackers)* [patch posted]`

`- **[bugs] [Logical replication silently drops rows on publisher restart under load](URL)** — confirmed regression in 17.2, bisected to commit abc1234; workaround posted, fix in progress. *(pgsql-hackers)* [open]`

`- **[Why is everyone suddenly moving off RDS?](URL)** — 300-comment HN thread trading cost and lock-in war stories; the substance is the migration tactics in the replies, not the headline. *(Hacker News · 300+ comments)*`

**Bad (filter out):**
`- "Acme DB raises $40M Series B to revolutionize the cloud-native AI-ready database" — funding announcement, no technical content. (excluded)`

`- **[general] How do I speed up my query?** — routine user question with no surprising answer. (excluded)`

## Keeping the skill healthy

The source list is the skill's memory. Treat `references/sources.md` as a living file: add what proves valuable, demote what turns into a billboard. Over a few months this should converge on a personal, high-trust set of sources tuned to what the reader actually finds worth reading.

**Quarterly source review (every 13 weeks, from `references/yield-stats.tsv`).** This is the mechanical counterpart to the paragraph above — it turns "demote what turns into a billboard" from a vibe into a number. Sum each outlet's `candidates` and `published` across the last 13 weekly rows.

Skip every `[pipe]` outlet entirely — a pipe's conversion measures the width of the entrance, not the quality of what's behind it, so it has nothing to say here.

Before marking anything, pull that outlet's rows from the local `references/ledger.tsv` and check the `reason_code` mix. If `DUPE` or `OFFTOPIC` dominate, the problem is on our side — a dedup gap or an imprecise query — fix that instead of touching the outlet's standing.

For `[solo]` outlets: 5+ candidates and 0 published over the quarter → tag `[low-yield]` and drop its scan priority one step (P1→P2, P2→P3). A second consecutive quarter at `[low-yield]` → tag `[dormant]` and remove it from the weekly scan. 0 candidates at all, for the whole quarter → straight to `[dormant]`.

For `[org]` outlets the bar is higher and the outcome is different, because there's no single editorial policy behind a multi-author blog to demote — judging the substance, not the domain (step 7) still applies post by post. 12+ candidates and ≤1 published over the quarter → tag `[low-yield]` — never `[dormant]`, an org outlet is never fully retired by this review. Note in the entry that scanning the whole blog isn't worth it, and: if the rare published items trace back to one or two regular authors, give those authors their own line in `references/sources.md` and their own feed in `references/feeds.opml`, and drop the corporate blog's own priority to P3.

`[low-yield]` and `[dormant]` are observations, not verdicts — don't invent other labels, and don't rewrite one already sitting on an entry from an earlier review.
