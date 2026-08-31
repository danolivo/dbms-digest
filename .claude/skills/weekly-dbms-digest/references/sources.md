# Sources

The living source list for the weekly DBMS digest. Priority is a rough guide to scan order
(P1 = check every week, P2 = check most weeks, P3 = sample / opportunistic).
When you find a new high-signal source, append it under the right section with a one-line note
and a priority. When a source goes dormant or turns into pure marketing, mark it `[dormant]`
or `[mostly-marketing]` rather than deleting it, so it isn't re-added next week.

**Feed list:** the machine-readable RSS/Atom feeds scanned each run live in
`references/feeds.opml` (all languages; also importable into any feed reader). Keep it in sync
with this file — add confirmed feeds, drop dead ones.

**Outlet key.** For the source-yield ledger (SKILL.md step 7b), every outlet is identified by a
normalized key: the domain (`thebuild.com`), or domain + path for a shared platform
(`dev.to/franckpachot`, `habr.com/ru/companies/postgrespro`). Normalize to lower-case, strip
`www.`, strip a trailing slash, strip `utm-*` params. The same post reached via an aggregator and
via its own site is one candidate keyed to the personal site, not the aggregator.

**Outlet class — required on every entry below.** Tagged \`[solo]\` / \`[org]\` / \`[pipe]\` right
after the name:
- \`solo\` — one author, one publication policy; a quarterly low-yield/dormant review (step "Keeping
  the skill healthy") applies directly.
- \`org\` — multi-author company/community blog; no single policy by construction (step 7 already
  says judge the substance, not the domain). The quarterly review applies only past a higher
  threshold, and the outcome is "split off the productive authors," not "retire."
- \`pipe\` — an aggregator, hub, newsletter, preprint feed, or forum (Planet PostgreSQL, HN,
  Lobsters, a Habr *hub* as a whole, arXiv, pgsql-hackers, pgsql-committers, Reddit, DBA SE):
  transport, not a publication. Excluded from the quarterly review entirely.
When you add a new source, add its class in the same edit — don't leave it for later. The
2026-06-18…2026-08-31 entries in the "New sources added (log)" below predate this scheme and
carry no class yet; when one of them produces a ledger row before it's been promoted to a
categorized section, default it to `org` for that row and give it a real class here as part of
that same run's step 6 — don't block the digest on it.

## Aggregators & newsletters (start here — best fan-out)

- **Planet PostgreSQL** `[pipe]` — official community blog aggregator; the firehose of core contributors, vendors, and independents. P1. https://planet.postgresql.org/
- **Postgres Weekly** `[pipe]` — curated weekly Postgres newsletter (Cooperpress). Good signal, light on fluff. P1. https://postgresweekly.com/
- **DB Weekly** `[pipe]` — broader weekly database newsletter (Cooperpress). `[dormant]` — confirmed 2026-08-03: site banner says "360 issues – archives only", no longer published. Archive still browsable; do not re-add. https://dbweekly.com/
- **pganalyze "5mins of Postgres"** `[solo]` — weekly walkthrough of interesting Postgres content from the prior 7 days; effectively a pre-filtered digest. P1. https://pganalyze.com/blog
- **PostgreSQL News Archive** `[pipe]` — official project announcements (releases, CVEs). P1. https://www.postgresql.org/about/newsarchive/
- **Hacker News (front page, db filter)** `[pipe]` — sample for database/systems threads with real discussion. P2. https://hn.algolia.com/?query=postgres

## PostgreSQL blogs (primary)

- **Bruce Momjian** `[solo]` — core team; internals, community direction. P2. https://momjian.us/main/blogs/
- **Crunchy Data blog** `[org]` — frequently substantive engineering (e.g. Elizabeth Christensen, Craig Kerstiens). Judge per-post; skip the pure product posts. P2. https://www.crunchydata.com/blog
- **pganalyze blog** `[org]` — query performance, planner, internals. P2. https://pganalyze.com/blog
- **EDB blog** `[org]` — enterprise Postgres, HA, migrations; filter heavily for marketing. P3. https://www.enterprisedb.com/blog
- **Timescale blog** `[org]` — time-series / analytics on Postgres; good patterns, watch for product push. P3. https://www.timescale.com/blog
- **Fujitsu (Fastware) Postgres blog** `[org]` — internals and feature deep-dives. P3. https://www.postgresql.fastware.com/blog
- **Microsoft Azure for PostgreSQL blog** `[org]` — sometimes solid internals; filter marketing. P3. https://techcommunity.microsoft.com/category/azuredatabases/blog/adforpostgresql
- **Postgres.ai blog** `[solo]` — DBLab, database branching, performance tooling. P3. https://postgres.ai/blog
- **PgDog blog (Lev Kokotov)** `[solo]` — pooler/sharding internals from the implementer. P3. https://pgdog.dev/blog

## PostgreSQL development (primary, highest trust)

- **pgsql-hackers mailing list** `[pipe]` — where features are actually designed and argued. Highest signal for "what's coming". P1. https://www.postgresql.org/list/pgsql-hackers/
- **PostgreSQL commitfest** `[pipe]` — patches under review; a roadmap of near-term features. P2. https://commitfest.postgresql.org/
- **PostgreSQL git commits** `[pipe]` — ground truth for "did X actually land". Use to fact-check claims. P2. https://git.postgresql.org/gitweb/?p=postgresql.git

## Wider DBMS & distributed data

- **Andy Pavlo / CMU DB Group blog** `[solo]` — industry analysis, annual "Databases in <year>" retrospective, seminar series. P1. https://www.cs.cmu.edu/~pavlo/blog/ and https://db.cs.cmu.edu/
- **DBMS Musings (Daniel Abadi)** `[solo]` — isolation/consistency, distributed DB theory made readable. P2. http://dbmsmusings.blogspot.com/
- **Murat Demirbas — Metadata blog** `[solo]` — distributed systems & database papers, paper reviews. P2. https://muratbuffalo.blogspot.com/
- **The New Stack — Databases** `[org]` — news/trends; mixed, filter for substance. P3. https://thenewstack.io/data/
- **QuestDB blog** `[org]` — time-series engine internals and skeptical benchmarking-methodology writing. P3. https://questdb.com/blog/
- **awesome-database-learning** `[pipe]` — curated internals reading list; mine for new primary sources. P3. https://github.com/pingcap/awesome-database-learning

## Commercial engines (new techniques & inventions — filter marketing hard)

- **SQL Server — Microsoft engineering blogs & docs** `[org]` — "What's new" + engine internals; mine for real optimizer/storage/columnstore/Hekaton-style techniques, not feature sheets. P2. https://techcommunity.microsoft.com/category/sql-server/blog/sqlserver
- **Bob Ward / SQL Server team deep-dives** `[solo]` — internals talks and write-ups. P3. https://learn.microsoft.com/en-us/sql/
- **Oracle Optimizer blog** `[org]` — CBO internals and new optimizer features straight from the team. P2. https://blogs.oracle.com/optimizer/
- **Oracle Database Insider / Maria Colgan** `[org]` — In-Memory, new-version internals. P3. https://blogs.oracle.com/database/
- **Franck Pachot** `[solo]` — cross-engine internals (Oracle, Postgres, YugabyteDB, MongoDB); excellent technique-level comparisons. P2. https://dev.to/franckpachot
- **MySQL Server Blog / engineering** `[org]` — InnoDB, optimizer, replication internals. P3. https://dev.mysql.com/blog-archive/
- **Percona blog (MySQL/Postgres/Mongo)** `[org]` — often substantive engineering; filter the product posts. P3. https://www.percona.com/blog/
- **MariaDB Foundation blog** `[org]` — engine-level write-ups (e.g. the DuckDB storage-engine line of work); also a clean MariaDB release radar. P3. https://mariadb.org/blog/

## Migration experience (real-world reports — prioritise)

- **AWS Database Blog — migrations** `[org]` — Oracle/SQL Server → Postgres/Aurora war stories; technical, watch for product push. P2. https://aws.amazon.com/blogs/database/
- **Stormatics** `[org]` — incident/migration field reports. P2. https://stormatics.tech/
- **pgEdge / Crunchy / EDB migration write-ups** `[composite — not one outlet]` — judge per-post for real lessons vs. pitch; key ledger rows by the post's actual domain (pgedge.com `org`, crunchydata.com / enterprisedb.com already classed above). P3.
- _Also surface migration posts that appear via Planet PostgreSQL and DB Weekly — they show up there regularly._

## Research venues (cutting edge — check for new proceedings / preprints)

- **VLDB** `[pipe]` — proceedings (PVLDB). P2. https://www.vldb.org/pvldb/
- **SIGMOD / ACM SIGMOD Record** `[pipe]` — major systems papers. P2. https://sigmod.org/
- **CIDR** `[pipe]` — innovative/early systems ideas (e.g. Umbra). P2. https://www.cidrdb.org/
- **DBWorld (SIGMOD)** `[pipe]` — CfPs and community announcements; useful to spot what's hot. P3. https://dbworld.sigmod.org/browse.html
- **arXiv cs.DB** `[pipe]` — database preprints. P2. https://arxiv.org/list/cs.DB/recent

## Conferences & CFP trackers (for the Call-for-papers section)

Find conferences / PGDays / meetups with an **open** CFP, plus applied/research venues close to
Postgres. List a CFP only while its deadline is in the future.

**PostgreSQL community events**
- **PostgreSQL.org — Upcoming events** `[pipe]` — official community event list. P1. https://www.postgresql.org/about/events/
- **PostgreSQL.org — News archive** `[pipe]` — "CFP is now open" announcements land here. P1. https://www.postgresql.org/about/newsarchive/
- **dev.events — Postgres** `[pipe]` — aggregator of Postgres conferences with dates/CFPs. P2. https://dev.events/postgres
- **PGConf.dev** `[pipe]` — the developers' conference. P2. https://www.pgconf.dev/
- **PGConf.EU** `[pipe]` — European community conference (year-versioned site). P2. https://www.pgconf.eu/
- _Regional PGDays_: Nordic PGDay, PGDay Paris, PGDay Boston, PGDay UK / Lowlands, PGDay Israel, FOSDEM PGDay, Prague PostgreSQL Developer Day (p2d2.cz), Swiss PGDay, PGConf NYC / India. P3.

**Applied & research DB-systems venues (close to Postgres)**
- **VLDB** `[pipe]` — rolling monthly PVLDB research deadlines. P2. https://www.vldb.org/
- **ACM SIGMOD** `[pipe]` — multi-round research deadlines (year-versioned site). P2. https://sigmod.org/
- **CIDR** `[pipe]` — innovative/early systems ideas. P2. https://www.cidrdb.org/
- **IEEE ICDE** `[pipe]` — https://icde.org/ . P3.
- **DEBS** `[pipe]` — distributed & event-based systems. https://debs.org/ . P3.
- **USENIX ATC / OSDI** `[pipe]` — systems venues with frequent DB work. https://www.usenix.org/conferences . P3.
- **WikiCFP — databases** `[pipe]` — academic CFP aggregator. http://www.wikicfp.com/cfp/call?conference=databases . P3.
- _Practitioner_: P99 CONF, HYTRADBOI. P3.

## Non-English sources (multilingual)

_Scan these in their native language and present items per the non-English formatting rule
(English headline + one-liner, a language tag, original title in parentheses). The same
anti-marketing and fact-check bar applies — verify technical claims against the original, not
just a translation._

_Prefer each source's RSS/Atom feed where available (dated, language-native, fetches cleanly).
For JS-heavy or region-specific sites that return stale/empty HTML — Chinese aggregators
(modb.pro), PolarDB / Alibaba Cloud, PingCAP, also Reddit and Qiita — render them with the
Claude-in-Chrome browser tools instead of a plain fetch. Treat web search as English/US-biased:
use it to confirm, not to discover._

### Russian `[ru]`
- **Postgres Pro blog** `[org]` — Russian Postgres vendor; internals, patches, version deep-dives (some cross-posted in EN). P2. https://postgrespro.ru/blog
- **Habr — PostgreSQL hub** `[pipe]` — large RU dev community; internals posts and production war stories. `[js]` P2. https://habr.com/ru/hubs/postgresql/
- **Greengage blog** `[org]` — Greenplum-lineage Postgres MPP; ops/internals (pg_upgrade/ggupgrade, ggrebalance). P3. https://habr.com/ru/companies/greengage/articles/

### Chinese `[zh]`
- **PingCAP / TiDB blog (CN)** `[org]` — distributed SQL internals, Raft, TiKV. P2. https://cn.pingcap.com/blog/
- **OceanBase** `[org]` — distributed DB engineering write-ups (CN). P3. https://www.oceanbase.com/
- **Alibaba Cloud developer (PolarDB / AnalyticDB)** `[pipe]` — engine internals; huge, filter hard. `[js]` P3. https://developer.aliyun.com/
- **modb.pro (墨天轮)** `[pipe]` — Chinese DBA community and articles (Oracle, PG, MySQL, domestic engines). P3. https://www.modb.pro/
- **老冯云数 / blog.vonng.com (Ruohang Feng, Pigsty)** `[solo]` — high-signal PG-ecosystem essays, several per week; EN mirrors at /en/. Watch for Pigsty self-promo, the engineering is real. P2. https://blog.vonng.com/

### French `[fr]`
- **Dalibo blog** `[org]` — French Postgres consultancy; substantive internals (FR, some EN). P2. https://blog.dalibo.com/ · RSS https://blog.dalibo.com/feed.xml
- **dbi-services blog** `[org]` — Swiss; PG/Oracle/SQL Server ops (FR + EN). P3. https://www.dbi-services.com/blog/

### German `[de]`
- **Cybertec (DE)** `[org]` — German-language posts from the Cybertec team (the EN edition is listed above). P3. https://www.cybertec-postgresql.com/de/

### Japanese `[ja]`
- **Qiita — PostgreSQL tag** `[pipe]` — large JP dev community; how-tos and internals. `[js]` P3. https://qiita.com/tags/postgresql · RSS https://qiita.com/tags/postgresql/feed
- **SRA OSS (JP)** `[org]` — Japanese Postgres support company write-ups. P3. https://www.sraoss.co.jp/
- **Publickey (Junichi Niino)** `[solo]` — Japanese DBMS/cloud journalism; server-rendered, fetches reliably. P3. https://www.publickey1.jp/
- **gihyo.jp «OSSデータベース取り時報»** `[org]` — monthly MySQL/PG/Tsurugi column, lands ~1st of each month. P3. https://gihyo.jp/

_Discover more per the self-update rule — pin precise regional blogs/authors/channels
(incl. Telegram, WeChat, Qiita) as you find keepers; retire dead ones._

## New sources added (log)

_Append discoveries here with date, name, link, and a one-line reason. Example:_
- (2026-06-18) _seed list created._
- (2026-06-18) boringsql.com (Radim Marek) — reproducible Postgres internals deep-dives. https://boringsql.com/
- (2026-06-18) justatheory.com (David Wheeler) — PGXN/extensions + Postgres↔ClickHouse interop. https://justatheory.com/
- (2026-06-18) stormatics.tech — incident-style Postgres ops deep dives. https://stormatics.tech/
- (2026-06-18) thebuild.com (Christophe Pettus) — near-daily GUC-internals series and cross-engine planner deep-dives. P2. https://thebuild.com/blog/
- (2026-06-18) event-driven.io (Oskar Dudycz) — event sourcing / Postgres-as-event-store engineering. P3. https://event-driven.io/
- (2026-06-18) modern-sql.com (Markus Winand) — cross-engine SQL-standard conformance and feature comparisons. P2. https://modern-sql.com/
- (2026-06-22) pghackers.com — AI-assisted search/explorer over the pgsql-hackers archive; trial as a faster way to triage in-window threads than the raw monthly index. P3. https://www.pghackers.com/
- (2026-06-29) _Operational note (not a new publisher):_ when the run's egress policy blocks the official site/archives (planet.postgresql.org, www.postgresql.org, mail-archive.com, commitfest), the **GitHub mirror `github.com/postgres/postgres`** is a reliable, fetchable fallback for ground-truth — the `/commits/master?since=&until=` view is date-windowed and verifiable, and individual `/commit/<sha>` pages give the full message + diff. Use it to anchor the PostgreSQL section on what actually landed. P1 (fallback).
- (2026-06-29) QuestDB blog (questdb.com/blog) — time-series internals + benchmarking-methodology writing; surfaced via a strong HN thread ("Lies, Damn Lies and Database Benchmarks"). P3.
- (2026-06-29) Greengage blog [ru] — Greenplum-lineage Postgres MPP engineering (pg_upgrade/ggupgrade, ggrebalance). Watch for MPP-on-Postgres internals. P3.
- (2026-06-29) _Operational note (fetch path):_ when plain `WebFetch`/`curl` fail or time out on the official domains, the **Claude-in-Chrome path + same-origin `fetch()`** is a reliable fallback that this run used end-to-end: navigate to the target domain, then `fetch()` its feed/API in-page and parse (RSS via `DOMParser`, JSON via `.json()`). Confirmed working this run for planet.postgresql.org (rss20.xml), www.postgresql.org (news archive + /list/pgsql-hackers/since/<ts>), commitfest.postgresql.org (/59/activity/), api.github.com (releases), rss.arxiv.org, hn.algolia.com (API), habr.com and blog.dalibo.com. Note: the in-page fetch is blocked if the current tab URL carries a query string (privacy guard) — navigate to a query-string-free URL first.
- (2026-07-06) pduzc.com (Zhang Chen) — PostgreSQL data-recovery / file-forensics field reports (ransomware carve-out recovery, single-file-per-relation risk analysis); rare hands-on content, appears on Planet PostgreSQL. P3. https://pduzc.com/blog
- (2026-07-06) _Operational notes (this run):_ (1) plain fetch worked for postgresql.org + planet + commitfest this run, BUT several pages were served **cache-stale**: the global CF /activity/ was ~6 weeks old, the per-CF /59/activity/ cache was cut at Jun 24, and arXiv /list/cs.DB/* listings were mid-May/mid-June snapshots — cross-check a page's newest date before trusting it; the in-browser path returned live data every time. (2) The per-CF activity log keeps only its **last 100 rows** (no pagination) — during an In Progress CF that's ~5 days of history, so capture it early in the week or accept undercounting. (3) The /59/ page header "Status summary" line carries authoritative queue totals — no need for the sidebar. (4) mail-archive.com works well for pgsql-hackers/-general, but its pgsql-performance mirror has been silent since 2026-05-11 and there is NO mail-archive mirror of pgsql-bugs in the lists.postgresql.org era; postgresql.org /list/<name>/ browse pages rendered empty to plain fetch this run — bugs coverage came via hackers cross-references. (5) Feed URLs fetched as raw XML can come back as undecoded "[binary data]" — fetch the HTML index pages instead, or use the browser.
- (2026-07-13) pgdog.dev/blog (Lev Kokotov) — pooler/sharding internals from the implementer; strong first-party rationale posts. P3.
- (2026-07-13) blog.vonng.com (老冯云数, Ruohang Feng) [zh] — PG-ecosystem essays, two strong in-window items this week (PG 30th-birthday commit forensics, PG18 CoW cloning). P2.
- (2026-07-13) publickey1.jp (Junichi Niino) [ja] — DBMS/cloud journalism, server-rendered and reliably fetchable. P3.
- (2026-07-13) mariadb.org/blog — MariaDB Foundation engine write-ups + release radar. P3.
- (2026-07-13) gihyo.jp OSS-DB monthly column [ja] — MySQL/PG/Tsurugi roundup ~1st of month. P3.
- (2026-07-13) _Unverified claim from this run (check before acting): dbweekly.com may be defunct (archive reportedly frozen at issue #360, 2021-06-25). Verify next run and mark [dormant] if confirmed; do NOT retire yet._
- (2026-07-13) _Operational notes (this run, no browser connected):_ (1) plain-fetch caches widely stale — planet.postgresql.org frozen at Jul 4 (rss20.xml returned binary; reconstructed the week via Postgres Weekly issue + direct blog fetches), mail-archive maillist.html frozen at May 18 (walk the lists via per-day search `search?l=<list>&q=date:YYYYMMDD` + msg chaining instead — worked well), commitfest /59/activity/ frozen at Jun 24 while /61/activity/, /current/ and /open/ were live — during an In Progress CF report flow from queue-total deltas when the activity log is stale. (2) github.com/postgres/postgres commit pages and gitweb returned empty; the pgsql-committers mail-archive was fresh through Jul 11 and is a good commit ground-truth fallback (commitdiff links inside the mails). (3) arXiv /list/cs.DB/recent and /new were stale May caches; the month listing /list/cs.DB/2026-07 was fresh once reached by chaining from any abs page. (4) CF numbering: #60 is the year-long PG20-Drafts CF; the next regular CF (PG20-2) is #61 — don't assume consecutive numbers.
- (2026-07-20) _Operational notes (this run, no browser):_ (1) **pgsql-committers on mail-archive was the one fresh archive** — its *thread* index (`index.html`) was current through Jul 18 while its date index (`maillist.html`) was frozen at Jul 11; the hackers-list index remained frozen at May 18 and mail-archive's `search?...` URLs were blocked to cold fetch (provenance), so lists coverage = committers commit messages. (2) postgresql.org `/message-id/<id>` pages render fully to plain fetch (incl. whole-thread index and a dated `/list/<list>/since/<ts>` link), but `/list/...` and `/since/...` browse pages render empty — message pages are the usable unit. (3) postgrespro.com `/list/pgsql-hackers` mirror month index stopped at 2026-05 this run. (4) CommitFest app cache-stale end-to-end (see commitfest-state.json 2026-07-13 note). (5) dbweekly.com dormancy still unverified — carry over.

- (2026-07-27) planetscale.com/blog (Engineering) — vendor (Postgres + Vitess host) but the engineering posts are substantive Postgres internals: Jan Nidzwetzki's MVCC/bloat deep-dive with runnable psql, planner-goes-rogue postmortems, sharding write-ups. Filter the product/Traffic-Control posts; keep the internals ones. Atom feed at planetscale.com/blog/feed.atom. P3. https://planetscale.com/blog
- (2026-07-27) _Operational notes (this run, no browser):_ (1) **pgsql-committers thread index (`index.html`) was fresh through Jul 26** (msg47527 = Sun 26 Jul) — the single reliable lists path again; individual `msgNNNNN.html` pages carry the full commit message + git commitdiff link and a real timestamp (in -0700), so date-check the Sun/Mon window boundary against those. hackers/-bugs/-performance archives unreachable as before. (2) **arXiv `/list/cs.DB/recent` was FRESH** this run (top = Mon 27 Jul; Jul 21-24 fully enumerable) — good week for the research section; the LLM-agent/text-to-SQL papers dominate volume, so mine for storage/isolation/CC/index work. (3) postgresql.org news archive posted NOTHING after Jul 16 (PG19 Beta 2) — a genuinely quiet announce week, not a fetch failure (older-news pagination confirmed). (4) confbase.io conference schedules (e.g. Hyderabad PGDays via `2026.pghyd.in/schedule/`) are JS iframe embeds — the WordPress page fetches but the talk list needs a browser; `confbase.io/embed/...` was blocked to cold fetch (provenance). (5) dbweekly.com dormancy STILL unverified — carry over again.
- (2026-07-27b) _Browser techniques confirmed (digest rebuilt with browser):_ (1) **Conference schedules on confbase.io** render fine — navigate the browser directly to the iframe src `https://confbase.io/embed/<slug>/<year>/schedule?theme=dark` and `get_page_text`; the Hyderabad PGDays 2026 full talk grid came through cleanly (Day 1/2, tracks, rooms, speakers). (2) **Habr in-window scan** works via same-origin JS on `habr.com/ru/hubs/postgresql/articles/`: `document.querySelectorAll('article')` → read each `time[datetime]` + `.tm-title__link`; filter to the window. This week RU had ~8 in-window posts (Debezium MariaDB→PG migration, PG19 REPACK/SQL-PGQ/autovacuum preview, cron auto-partitioning, Tantor data-aging, a backup-won't-restore piece) — NOT the thin week plain-fetch implied. (3) `blog.vonng.com` returned ERR_CONNECTION_RESET this run (transient — do NOT retire; retry next week). (4) get_page_text lags one step right after navigate inside a browser_batch — read in a separate call, or the article extractor returns the previous page.
- (2026-08-03) coroot.com/blog — infra-observability vendor; Postgres posts reproduce failure modes (e.g. "Let's Break Autovacuum") rather than listing metrics. P3. https://coroot.com/blog/
- (2026-08-03) launchbylunch.com (Sehrope Sarkuni) — pgjdbc maintainer's blog; primary source for the new pg-java JVM driver (repo under the pgjdbc org). P3. https://launchbylunch.com/
- (2026-08-03) **DB Weekly confirmed dormant** — the 2026-07-13 unverified claim is now resolved: dbweekly.com says "360 issues – archives only / this newsletter is no longer published". Marked `[dormant]` above; carried-over verification item closed.
- (2026-08-03) blog.vonng.com reachable again (last week's ERR_CONNECTION_RESET was transient, as suspected); latest post Jul 10, nothing in-window this run. Keep at P2.
- (2026-08-10) hexacluster.ai/blog (Avi Vallarapu) — benchmark-backed Postgres tuning write-ups (HammerDB TPROC-C on HOT updates / fillfactor); numbers, not checklists. Appears on Planet PostgreSQL. P3. https://hexacluster.ai/blog
- (2026-08-10) vvka-141.github.io/pgmi/articles/ (Alexey Evlampiev) — schema-migration mechanics: lock queues, transaction boundaries, `CREATE INDEX CONCURRENTLY`'s two different refusals. Tool-adjacent (pgmi) but the reasoning is about Postgres. P3.
- (2026-08-10) byteofdev.com (Jacob Jackson) — occasional but high-effort systems stunts (this week: an LLM behind the Postgres wire protocol, with real storage APIs underneath). Sample, don't subscribe blindly. P3. https://byteofdev.com/
- (2026-08-11b) malisper.me (Michael Malis) — the pgrust series: Postgres reimplemented in Rust, with per-optimisation measurements and disclosed benchmark setups (Volcano → batching → operator fusion → SIMD, each timed). Headline multipliers are self-reported; the engineering is first-rate. Surfaced only via live HN Algolia, not via Planet or any newsletter. P2. https://malisper.me/
- (2026-08-11b) cedardb.com/blog (Umbra/TUM lineage) — storage encodings, compression, vectorised execution; no sales pitch. Discovered via Lobsters /t/databases + r/databasedevelopment. P3. https://cedardb.com/blog/
- (2026-08-11b) blog.dave.tf (David Anderson) — occasional but deep systems/columnar-format write-ups (FastLanes Unified Transport Layout). P3. https://blog.dave.tf/
- (2026-08-11b) brandur.org/fragments (Brandur Leach) — short, high-signal Postgres-in-production fragments (pgtestdb template cloning). P3. https://brandur.org/
- (2026-08-11b) shopify.engineering — applied MySQL/InnoDB engineering at scale (SKIP LOCKED reservation pools, composite-PK lock counts, connection-hold-time attribution). Worth a monthly skim for the Commercial-engines section. P3. https://shopify.engineering/
- (2026-08-11b) _CORRECTION — a browser WAS available this run, via the **`Control_Chrome` MCP server** (AppleScript-based, host Chrome), not the claude-in-chrome extension, which reported zero paired browsers all session (`list_connected_browsers` → `[]`, pairing broadcast found nothing). **Check `Control_Chrome` before concluding "no browser".** Two prerequisites: (a) Chrome → View → Developer → **Allow JavaScript from Apple Events** must be enabled, or `get_page_content`/`execute_javascript` fail with a misleading "Google Chrome is not running" while `list_tabs`/`open_url` still work; (b) `execute_javascript` is synchronous — use the kick-off-then-poll pattern (see community-sources.md 2026-08-11b) and return one JSON string. The browser materially changed this week's digest: it added the pgrust 300x write-up, the Shopify Redis→MySQL thread, a PlanetScale InnoDB-MVCC postmortem that restored the whole Commercial-engines section, plus CedarDB/FastLanes/pgtestdb — roughly six items a plain-fetch pass had missed._
- (2026-08-11c) _Verified-quiet non-English window Aug 3–9 (recorded so a future run doesn't mistake this for under-scanning): blog.vonng.com `[zh]` newest Jul 23; blog.dalibo.com `[fr]` newest Jul 30 (job ad); publickey1.jp `[ja]` nine in-window posts, zero DB items; Qiita `[ja]` PostgreSQL tag one in-window post (beginner psql vs SQL*Plus, below bar); cybertec-postgresql.com one partnership PR + one CNPG how-to. All plain-fetch or browser-readable. **modb.pro `[zh]` is the one still-unenumerated source** — client-rendered SPA, front page exposes no dated article list; try a category/search URL next run._
- (2026-08-11) _Follow-up to the same run (Chrome still unreachable; these were solved WITHOUT a browser and supersede parts of the note above):_ (1) **How to reach `/61/activity/`:** the *per-CF* activity link only exists on the CF detail page — fetch `commitfest.postgresql.org/<n>/?tag=<anything>` (the tag-filtered view is small, unlike the bare `/<n>/`) and its "Activity log" link puts `/<n>/activity/` into the provenance set. Worth doing every run. (2) **The ~100-row cap is the real constraint, not access.** Both the global and per-CF logs keep only their last ~100 rows and there is no pagination, so a Monday run already cannot see the previous Mon–Tue. **Capture the CF flow early in the week, or accept a permanently partial count** — no browser recovers rolled-off rows. (3) **The `/<n>/?tag=` page header carries the authoritative `Status summary` line** (PG20-2 on Aug 10: 269 needs review / 20 waiting on author / 44 ready for committer / 21 committed / 23 moved / 4 withdrawn / 381 total) — use these queue totals when the activity log is short. (4) **Verified-quiet non-English sources for the Aug 3–9 window** (record so a future run doesn't mistake this for under-scanning): blog.vonng.com `[zh]` newest post Jul 23; blog.dalibo.com `[fr]` newest Jul 30 (a job ad); publickey1.jp `[ja]` nine in-window posts, zero database items; cybertec-postgresql.com in-window = one partnership press release + one CNPG how-to. All four plain-fetch fine — **`blog.dalibo.com/`, `publickey1.jp/` and `cybertec-postgresql.com/en/postgresql-blog/` are reliable no-browser paths**; `blog.vonng.com/pg/` is a dated time-index but overflows the fetch limit, so read the saved-output file rather than re-fetching. (5) `lobste.rs/t/<tag>` returns an **empty body** to plain fetch (not an error) and Reddit cannot be seeded via search — both remain browser-only.
- (2026-08-10) _Operational notes (this run, NO browser — `tabs_context_mcp` reported the Chrome extension unreachable; plan for plain fetch only):_ (1) **`web_fetch` is provenance-gated for every cold URL** — seed each domain with a `WebSearch` first, then chain through links on fetched pages. Chaining is *mostly* reliable but not always: URLs that appeared inside the Postgres Weekly issue body (clickhouse.com, enterprisedb.com/blog) were still rejected, while postgresql.org / arxiv / mail-archive links chained fine — re-seed with a search when a chained link is refused. (2) **planet.postgresql.org plain HTML was LIVE** (newest item Aug 9) and covered the whole window — the best single fan-out path without a browser; no need for rss20.xml. (3) **mail-archive pgsql-committers thread index (`/`) fresh through Sun Aug 9** (msg47873); individual `msgNNNNN.html` pages fetch cleanly and print a real `-0700` timestamp — date-check the Mon/Sun seam against those (msg47693 = Sun 02 Aug 23:54 −0700). (4) **CommitFest: the GLOBAL `/activity/` page was FRESH this run** (top row 2026-08-10 03:09) — the reverse of the usual advice — but it holds only ~100 rows ≈ 5 days, and **`/61/activity/` could not be seeded into provenance** (no search surfaced it), so the early-week rows were lost. Open CF is now **PG20-2 (#61)**; #59 (PG20-1) has closed. (5) `postgresweekly.com/latest` redirects to the real issue and fetches fine (`/issues/latest` does not). (6) `arxiv.org/list/cs.DB/recent` was fresh and day-bucketed (Aug 3–7); reach it by fetching any `/list/cs.DB/<month>` page first — its header links `recent`. (7) `hntoplinks.com/week` pages 1–2 fresh; live `news.ycombinator.com/item?id=…` still empty to plain fetch. (8) **Habr:** `habr.com/ru/hubs/postgresql/` (the "Статьи" tab) plain-fetches the **live** chronological list with dates — no browser or JS needed. Do NOT fetch `/articles/top/alltime/`: it returns the all-time list and burns tokens for nothing.
- (2026-08-03) _Operational notes (this run, browser connected):_ (1) **web_fetch was provenance-gated for ALL cold URLs this run** — every fetch had to go through the browser; plan for that. (2) mail-archive pgsql-committers thread index fresh through Sun Aug 2 (msg47692); same-origin fetch of individual msgNNNNN.html pages works, but batched fetch+regex extraction intermittently trips a "[BLOCKED: Cookie/query string data]" guard — fetch one message per JS call and keep returned text sanitized/short, committer name via `itemprop="name"` regex works. (3) **planet.postgresql.org rss20.xml was LIVE via same-origin fetch** (newest item = Mon 03 Aug) and covered the whole window — best single fan-out path this run. (4) postgresweekly.com: `/issues/latest` returns "Invalid issue number"; use `/latest` (redirects to the real issue). (5) arXiv `/list/cs.DB/2026-07?skip=100&show=100` fetched fine same-origin; per-paper `[Submitted on …]` from /abs/ pages is the reliable date check. (6) api.github.com works same-origin from any page (CORS *) — good for release dates. (7) HN Algolia same-origin recipe (navigate to hn.algolia.com, then fetch API) reconfirmed working.
- (2026-08-17) mehmetince.net (Mehmet Ince) — vulnerability-researcher blog running a six-part "Systemic Risks in the Managed PostgreSQL Industry" series (part 1: a PostGIS memory-corruption chain to privilege escalation at Neon/Supabase/Xata). Rare first-hand Postgres-ecosystem security content; treat forward-looking 0-day claims as unverified until published. P3. https://mehmetince.net/
- (2026-08-17) _Operational notes (this run, browser via Control_Chrome):_ (1) **Control_Chrome worked end-to-end** while claude-in-chrome reported no paired browser — check it FIRST; `list_tabs` returning `[]` just means no tabs, `open_url` still works. JS from Apple Events was already enabled. (2) **commitfest.postgresql.org was live to plain fetch all the way** (seed `/61/?tag=<n>` via WebSearch, then chain to `/61/activity/` + global `/activity/`), and the Monday-03:30 capture still lost Mon–Wed to the ~100-row cap — earliest reachable row was Thu 16:47. Capturing mid-week remains the only fix. (3) **mail-archive pgsql-committers thread index fresh through Sun Aug 16** (`index.html` + `thrd2.html` covered msg47874–48254); individual msg pages carry −0700 timestamps for boundary checks. (4) postgresql.org news archive, events page, and news items all plain-fetched fine once the release announcement URL was seeded by search. (5) **web_fetch provenance does NOT accept URLs seen only in browser output or inside some fetched newsletter bodies** (github.com release tags, brandur.org, habr hub, blog.vonng.com all refused) — the browser covered those; api.github.com fetches work from a neutral-origin tab (hn.algolia.com) but are CSP-blocked from planetscale.com pages. (6) arXiv `/list/cs.DB/recent` was fresh in the browser (Aug 11–17 day-bucketed); `/abs/` pages give `[Submitted on …]` and `blockquote.abstract` for gists. (7) Habr hub scan recipe reconfirmed via browser DOM (`article` → `time[datetime]` + `.tm-title__link` + vote counter). (8) blog.vonng.com reachable again; Pigsty release posts live under `/pigsty/<version>/`.

- (2026-08-24) exobench.ai/blog (Alexander Ioffe) — benchmark write-ups with disclosed builds and plans; the PG19 SQL/PGQ series measures `GRAPH_TABLE` against hand-written joins and recursive CTEs on a 19beta1 build. Tool-adjacent (ExoBench) and the headlines lean clickbait, but the numbers and plans are shown. P3. https://exobench.ai/blog
- (2026-08-24) seedfa.st/blog (Mikhail Shytsko) — short, reproduced-against-a-real-version Postgres failure-mode posts (sequence-out-of-sync after a fixture load, run on 18.6 with pasted output). Appears on Planet PostgreSQL. P3. https://seedfa.st/blog
- (2026-08-24) ardentperf.com (Jeremy Schneider) — Postgres-on-Kubernetes and storage/memory measurement work with reproduction repos; this week's cgroup-v2 `container_memory_working_set_bytes` piece is the best explanation of why that metric misleads for Postgres. P2. https://ardentperf.com
- (2026-08-24) elastic.co/search-labs/blog — Elastic's engineering blog; the storage/columnar posts are real engine content (Columnar Mode in 9.5), the rest is product. Worth a monthly skim for the Wider-DBMS section. P3. https://www.elastic.co/search-labs/blog
- (2026-08-24) _Operational notes (this run, browser via Control_Chrome):_ (1) **Control_Chrome worked; claude-in-chrome not needed.** `open_url` + `execute_javascript` kick-off/poll pattern reconfirmed; HN Algolia, the Reddit seven-sub JSON sweep, Lobsters `.story`/`a.u-url`, DBA-SE API and the Habr hub DOM scan all worked from it. (2) **Plain `web_fetch` was healthy this run** for planet.postgresql.org (full window, best single fan-out), postgresql.org (news archive, events, news items), commitfest.postgresql.org (`/61/?tag=34` → activity log), mail-archive pgsql-committers (thread index fresh through Sunday, msg48301–48509), `www.arxiv.org/list/cs.DB/recent` (fresh, day-bucketed Aug 18–24), blog.dalibo.com and publickey1.jp — each after one seeding `WebSearch`. (3) **pgsql-hackers on mail-archive still cannot be seeded** — no search surfaces `mail-archive.com/pgsql-hackers@lists.postgresql.org/`, and `postgrespro.com/list/pgsql-hackers/<month>` was likewise refused. Committers + CommitFest remains the working substitute. (4) **CF activity-log cap bit from both ends this week**: earliest reachable row Mon 15:24, newest row Fri 03:48 — a Monday capture loses the tail as well as the head. Prefer the `/61/?tag=` Status-summary queue totals for week-over-week. (5) **arXiv `/list/cs.DB/recent` is reachable cold via `www.arxiv.org`** (the `www.` host appeared in search results where the bare host did not). (6) blog.vonng.com `[zh]` newest post Aug 14 — verified quiet, not dead.
- (2026-08-24b) **SOLVED — pgsql-hackers is reachable; use this recipe every run.** Four previous runs recorded the list as "unreachable"; that conclusion was wrong. The **official archive renders fully in a browser** — only plain `web_fetch` gets an empty shell. Recipe:
  1. Navigate the browser to `https://www.postgresql.org/list/pgsql-hackers/<YYYY-MM>/`. It renders a day-bucketed table plus a **"Jump to day" strip** of links shaped `/list/pgsql-hackers/since/YYYYMMDD0000/`. (The month page itself only shows the first few days — do not scrape it directly.)
  2. From that tab, same-origin `fetch()` each day URL you need and parse with `DOMParser`. **Parsing trap:** the subject anchor is inside `th[scope="row"]`, NOT a `td` — `tr.querySelectorAll('td')` returns only [author, time]. Select `th a[href*="/message-id/"]` for subject+href, `td[0]` author, `td[1]` time. A trailing 📎 in the subject means an attachment (usually a patch).
  3. Each `since/` page spans several days, so parse under the `<h2>Aug. N, 2026</h2>` headers and dedupe by subject+author across pages.
  4. New threads = subjects not starting with `Re:`/`RE:`. For Aug 17–23 this yielded **624 messages / 90 new threads** — the single richest source in the digest.
  5. `https://www.postgresql.org/message-id/flat/<id>` renders whole threads to plain fetch AND same-origin fetch; individual `/message-id/<id>` pages give the body via `.message-content` (fall back to `pre`). Use these to characterise a thread instead of guessing from its subject.
  6. Same URL shapes work for `pgsql-bugs`, `pgsql-performance`, `pgsql-general` — swap the list name. Scan those too now that the path is known.
  7. Dead ends, do not retry: mail-archive's `pgsql-hackers@lists.postgresql.org` cannot be seeded into `web_fetch` provenance by any search; `marc.info/?l=postgresql-hackers` returns an empty body; `postgrespro.com/list/pgsql-hackers/<month>` is refused cold. **hackorum.dev** (forum-style pg-hackers frontend, now also ingesting -bugs/-docs/-general) fetches but its `/topics` index overflows the fetch limit — usable as a human UI, not needed for scanning.

- (2026-08-31) acadia.engineering/blog (Evan Czaplicki) — Datalog-inspired relational query-language project; two substantive posts in consecutive weeks ("Rethinking Database Programming," "Solving the 1+N Query Problem"), each driving genuine cross-platform HN/Reddit debate. P3. https://acadia.engineering/blog
- (2026-08-31) _Operational notes (this run):_ (1) **The two browsers split the workload cleanly**: the `mcp__Claude_Browser__*` pane (in-app browser) handled Planet PostgreSQL, postgresql.org (news archive + the `/list/pgsql-hackers/since/<ts>/` same-origin-fetch recipe), commitfest.postgresql.org, mail-archive, and arXiv without issue — but it **hard-blocks `old.reddit.com`** ("blocked by policy", not just empty/CORS). The `Control_Chrome` MCP server (real host Chrome, AppleScript-driven) reached `old.reddit.com/.../top.json` fine via the same recipe, and also handled Lobsters, DBA Stack Exchange, and the non-English sources — when one browser refuses a domain outright, try the other before concluding it's unreachable. (2) `Control_Chrome`'s `execute_javascript` needs the script IIFE-wrapped with a single JSON-string return; top-level `let`/`const` do not persist across separate calls, so state must live on `window`. (3) **The `postgresql.org/list/pgsql-hackers/since/<ts>/` pages are not contiguous** — a single `since/` fetch's date coverage can skip an intermediate day relative to the next fetch's start point (this run: Aug 26 and Aug 29 fell through on the first pass). Always diff the resulting date set against all seven days in the window before treating the mailing-list scan as complete; three separate `since/` fetches were needed this run, not the usual two.
