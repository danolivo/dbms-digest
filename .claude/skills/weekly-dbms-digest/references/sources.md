# Sources

The living source list for the weekly DBMS digest. Priority is a rough guide to scan order
(P1 = check every week, P2 = check most weeks, P3 = sample / opportunistic).
When you find a new high-signal source, append it under the right section with a one-line note
and a priority. When a source goes dormant or turns into pure marketing, mark it `[dormant]`
or `[mostly-marketing]` rather than deleting it, so it isn't re-added next week.

**Feed list:** the machine-readable RSS/Atom feeds scanned each run live in
`references/feeds.opml` (all languages; also importable into any feed reader). Keep it in sync
with this file — add confirmed feeds, drop dead ones.

## Aggregators & newsletters (start here — best fan-out)

- **Planet PostgreSQL** — official community blog aggregator; the firehose of core contributors, vendors, and independents. P1. https://planet.postgresql.org/
- **Postgres Weekly** — curated weekly Postgres newsletter (Cooperpress). Good signal, light on fluff. P1. https://postgresweekly.com/
- **DB Weekly** — broader weekly database newsletter (Cooperpress); covers the wider DBMS world. P1. https://dbweekly.com/
- **pganalyze "5mins of Postgres"** — weekly walkthrough of interesting Postgres content from the prior 7 days; effectively a pre-filtered digest. P1. https://pganalyze.com/blog
- **PostgreSQL News Archive** — official project announcements (releases, CVEs). P1. https://www.postgresql.org/about/newsarchive/
- **Hacker News (front page, db filter)** — sample for database/systems threads with real discussion. P2. https://hn.algolia.com/?query=postgres

## PostgreSQL blogs (primary)

- **Bruce Momjian** — core team; internals, community direction. P2. https://momjian.us/main/blogs/
- **Crunchy Data blog** — frequently substantive engineering (e.g. Elizabeth Christensen, Craig Kerstiens). Judge per-post; skip the pure product posts. P2. https://www.crunchydata.com/blog
- **pganalyze blog** — query performance, planner, internals. P2. https://pganalyze.com/blog
- **EDB blog** — enterprise Postgres, HA, migrations; filter heavily for marketing. P3. https://www.enterprisedb.com/blog
- **Timescale blog** — time-series / analytics on Postgres; good patterns, watch for product push. P3. https://www.timescale.com/blog
- **Fujitsu (Fastware) Postgres blog** — internals and feature deep-dives. P3. https://www.postgresql.fastware.com/blog
- **Microsoft Azure for PostgreSQL blog** — sometimes solid internals; filter marketing. P3. https://techcommunity.microsoft.com/category/azuredatabases/blog/adforpostgresql
- **Postgres.ai blog** — DBLab, database branching, performance tooling. P3. https://postgres.ai/blog
- **PgDog blog (Lev Kokotov)** — pooler/sharding internals from the implementer. P3. https://pgdog.dev/blog

## PostgreSQL development (primary, highest trust)

- **pgsql-hackers mailing list** — where features are actually designed and argued. Highest signal for "what's coming". P1. https://www.postgresql.org/list/pgsql-hackers/
- **PostgreSQL commitfest** — patches under review; a roadmap of near-term features. P2. https://commitfest.postgresql.org/
- **PostgreSQL git commits** — ground truth for "did X actually land". Use to fact-check claims. P2. https://git.postgresql.org/gitweb/?p=postgresql.git

## Wider DBMS & distributed data

- **Andy Pavlo / CMU DB Group blog** — industry analysis, annual "Databases in <year>" retrospective, seminar series. P1. https://www.cs.cmu.edu/~pavlo/blog/ and https://db.cs.cmu.edu/
- **DBMS Musings (Daniel Abadi)** — isolation/consistency, distributed DB theory made readable. P2. http://dbmsmusings.blogspot.com/
- **Murat Demirbas — Metadata blog** — distributed systems & database papers, paper reviews. P2. https://muratbuffalo.blogspot.com/
- **The New Stack — Databases** — news/trends; mixed, filter for substance. P3. https://thenewstack.io/data/
- **QuestDB blog** — time-series engine internals and skeptical benchmarking-methodology writing. P3. https://questdb.com/blog/
- **awesome-database-learning** — curated internals reading list; mine for new primary sources. P3. https://github.com/pingcap/awesome-database-learning

## Commercial engines (new techniques & inventions — filter marketing hard)

- **SQL Server — Microsoft engineering blogs & docs** — "What's new" + engine internals; mine for real optimizer/storage/columnstore/Hekaton-style techniques, not feature sheets. P2. https://techcommunity.microsoft.com/category/sql-server/blog/sqlserver
- **Bob Ward / SQL Server team deep-dives** — internals talks and write-ups. P3. https://learn.microsoft.com/en-us/sql/
- **Oracle Optimizer blog** — CBO internals and new optimizer features straight from the team. P2. https://blogs.oracle.com/optimizer/
- **Oracle Database Insider / Maria Colgan** — In-Memory, new-version internals. P3. https://blogs.oracle.com/database/
- **Franck Pachot** — cross-engine internals (Oracle, Postgres, YugabyteDB, MongoDB); excellent technique-level comparisons. P2. https://dev.to/franckpachot
- **MySQL Server Blog / engineering** — InnoDB, optimizer, replication internals. P3. https://dev.mysql.com/blog-archive/
- **Percona blog (MySQL/Postgres/Mongo)** — often substantive engineering; filter the product posts. P3. https://www.percona.com/blog/
- **MariaDB Foundation blog** — engine-level write-ups (e.g. the DuckDB storage-engine line of work); also a clean MariaDB release radar. P3. https://mariadb.org/blog/

## Migration experience (real-world reports — prioritise)

- **AWS Database Blog — migrations** — Oracle/SQL Server → Postgres/Aurora war stories; technical, watch for product push. P2. https://aws.amazon.com/blogs/database/
- **Stormatics** — incident/migration field reports. P2. https://stormatics.tech/
- **pgEdge / Crunchy / EDB migration write-ups** — judge per-post for real lessons vs. pitch. P3.
- _Also surface migration posts that appear via Planet PostgreSQL and DB Weekly — they show up there regularly._

## Research venues (cutting edge — check for new proceedings / preprints)

- **VLDB** — proceedings (PVLDB). P2. https://www.vldb.org/pvldb/
- **SIGMOD / ACM SIGMOD Record** — major systems papers. P2. https://sigmod.org/
- **CIDR** — innovative/early systems ideas (e.g. Umbra). P2. https://www.cidrdb.org/
- **DBWorld (SIGMOD)** — CfPs and community announcements; useful to spot what's hot. P3. https://dbworld.sigmod.org/browse.html
- **arXiv cs.DB** — database preprints. P2. https://arxiv.org/list/cs.DB/recent

## Conferences & CFP trackers (for the Call-for-papers section)

Find conferences / PGDays / meetups with an **open** CFP, plus applied/research venues close to
Postgres. List a CFP only while its deadline is in the future.

**PostgreSQL community events**
- **PostgreSQL.org — Upcoming events** — official community event list. P1. https://www.postgresql.org/about/events/
- **PostgreSQL.org — News archive** — "CFP is now open" announcements land here. P1. https://www.postgresql.org/about/newsarchive/
- **dev.events — Postgres** — aggregator of Postgres conferences with dates/CFPs. P2. https://dev.events/postgres
- **PGConf.dev** — the developers' conference. P2. https://www.pgconf.dev/
- **PGConf.EU** — European community conference (year-versioned site). P2. https://www.pgconf.eu/
- _Regional PGDays_: Nordic PGDay, PGDay Paris, PGDay Boston, PGDay UK / Lowlands, PGDay Israel, FOSDEM PGDay, Prague PostgreSQL Developer Day (p2d2.cz), Swiss PGDay, PGConf NYC / India. P3.

**Applied & research DB-systems venues (close to Postgres)**
- **VLDB** — rolling monthly PVLDB research deadlines. P2. https://www.vldb.org/
- **ACM SIGMOD** — multi-round research deadlines (year-versioned site). P2. https://sigmod.org/
- **CIDR** — innovative/early systems ideas. P2. https://www.cidrdb.org/
- **IEEE ICDE** — https://icde.org/ . P3.
- **DEBS** — distributed & event-based systems. https://debs.org/ . P3.
- **USENIX ATC / OSDI** — systems venues with frequent DB work. https://www.usenix.org/conferences . P3.
- **WikiCFP — databases** — academic CFP aggregator. http://www.wikicfp.com/cfp/call?conference=databases . P3.
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
- **Postgres Pro blog** — Russian Postgres vendor; internals, patches, version deep-dives (some cross-posted in EN). P2. https://postgrespro.ru/blog
- **Habr — PostgreSQL hub** — large RU dev community; internals posts and production war stories. `[js]` P2. https://habr.com/ru/hubs/postgresql/
- **Greengage blog** — Greenplum-lineage Postgres MPP; ops/internals (pg_upgrade/ggupgrade, ggrebalance). P3. https://habr.com/ru/companies/greengage/articles/

### Chinese `[zh]`
- **PingCAP / TiDB blog (CN)** — distributed SQL internals, Raft, TiKV. P2. https://cn.pingcap.com/blog/
- **OceanBase** — distributed DB engineering write-ups (CN). P3. https://www.oceanbase.com/
- **Alibaba Cloud developer (PolarDB / AnalyticDB)** — engine internals; huge, filter hard. `[js]` P3. https://developer.aliyun.com/
- **modb.pro (墨天轮)** — Chinese DBA community and articles (Oracle, PG, MySQL, domestic engines). P3. https://www.modb.pro/
- **老冯云数 / blog.vonng.com (Ruohang Feng, Pigsty)** — high-signal PG-ecosystem essays, several per week; EN mirrors at /en/. Watch for Pigsty self-promo, the engineering is real. P2. https://blog.vonng.com/

### French `[fr]`
- **Dalibo blog** — French Postgres consultancy; substantive internals (FR, some EN). P2. https://blog.dalibo.com/ · RSS https://blog.dalibo.com/feed.xml
- **dbi-services blog** — Swiss; PG/Oracle/SQL Server ops (FR + EN). P3. https://www.dbi-services.com/blog/

### German `[de]`
- **Cybertec (DE)** — German-language posts from the Cybertec team (the EN edition is listed above). P3. https://www.cybertec-postgresql.com/de/

### Japanese `[ja]`
- **Qiita — PostgreSQL tag** — large JP dev community; how-tos and internals. `[js]` P3. https://qiita.com/tags/postgresql · RSS https://qiita.com/tags/postgresql/feed
- **SRA OSS (JP)** — Japanese Postgres support company write-ups. P3. https://www.sraoss.co.jp/
- **Publickey (Junichi Niino)** — Japanese DBMS/cloud journalism; server-rendered, fetches reliably. P3. https://www.publickey1.jp/
- **gihyo.jp «OSSデータベース取り時報»** — monthly MySQL/PG/Tsurugi column, lands ~1st of each month. P3. https://gihyo.jp/

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