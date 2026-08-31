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

**Outlet class — required on every entry below.** Tagged `[solo]` / `[org]` / `[pipe]` right
after the name:
- `solo` — one author, one publication policy; a quarterly low-yield/dormant review (step "Keeping
  the skill healthy") applies directly.
- `org` — multi-author company/community blog; no single policy by construction (step 7 already
  says judge the substance, not the domain). The quarterly review applies only past a higher
  threshold, and the outcome is "split off the productive authors," not "retire."
- `pipe` — an aggregator, hub, newsletter, preprint feed, or forum (Planet PostgreSQL, HN,
  Lobsters, a Habr *hub* as a whole, arXiv, pgsql-hackers, pgsql-committers, Reddit, DBA SE):
  transport, not a publication. Excluded from the quarterly review entirely.
When you add a new source, add its class in the same edit — don't leave it for later. The
"New sources added (log)" section at the bottom holds only outlets still awaiting a class —
right now four (hexacluster.ai/blog, exobench.ai/blog, seedfa.st/blog, acadia.engineering/blog),
each a company blog with what looks like one steady author, so solo vs. org is the owner's call
to make. Resolve these before relying on a ledger row for them — there is no default-class
fallback in SKILL.md step 7b to fall back on.

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
- **PgDog blog (Lev Kokotov)** `[solo]` — pooler/sharding internals from the implementer; strong first-party rationale posts. P3. https://pgdog.dev/blog
- **boringsql.com (Radim Marek)** `[solo]` — reproducible Postgres internals deep-dives. P3 `[prio-unset]`. https://boringsql.com/
- **justatheory.com (David Wheeler)** `[solo]` — PGXN/extensions + Postgres↔ClickHouse interop. P3 `[prio-unset]`. https://justatheory.com/
- **event-driven.io (Oskar Dudycz)** `[solo]` — event sourcing / Postgres-as-event-store engineering. P3. https://event-driven.io/
- **pduzc.com (Zhang Chen)** `[solo]` — PostgreSQL data-recovery / file-forensics field reports (ransomware carve-out recovery, single-file-per-relation risk analysis); rare hands-on content, appears on Planet PostgreSQL. P3. https://pduzc.com/blog
- **launchbylunch.com (Sehrope Sarkuni)** `[solo]` — pgjdbc maintainer's blog; primary source for the new pg-java JVM driver (repo under the pgjdbc org). P3. https://launchbylunch.com/
- **vvka-141.github.io/pgmi/articles/ (Alexey Evlampiev)** `[solo]` — schema-migration mechanics: lock queues, transaction boundaries, `CREATE INDEX CONCURRENTLY`'s two different refusals. Tool-adjacent (pgmi) but the reasoning is about Postgres. P3. https://vvka-141.github.io/pgmi/articles/
- **byteofdev.com (Jacob Jackson)** `[solo]` — occasional but high-effort systems stunts (this week: an LLM behind the Postgres wire protocol, with real storage APIs underneath). Sample, don't subscribe blindly. P3. https://byteofdev.com/
- **malisper.me (Michael Malis)** `[solo]` — the pgrust series: Postgres reimplemented in Rust, with per-optimisation measurements and disclosed benchmark setups (Volcano → batching → operator fusion → SIMD, each timed). Headline multipliers are self-reported; the engineering is first-rate. Surfaced only via live HN Algolia, not via Planet or any newsletter. P2. https://malisper.me/
- **brandur.org/fragments (Brandur Leach)** `[solo]` — short, high-signal Postgres-in-production fragments (pgtestdb template cloning). P3. https://brandur.org/
- **mehmetince.net (Mehmet Ince)** `[solo]` — vulnerability-researcher blog running a six-part "Systemic Risks in the Managed PostgreSQL Industry" series (part 1: a PostGIS memory-corruption chain to privilege escalation at Neon/Supabase/Xata). Rare first-hand Postgres-ecosystem security content; treat forward-looking 0-day claims as unverified until published. P3. https://mehmetince.net/
- **ardentperf.com (Jeremy Schneider)** `[solo]` — Postgres-on-Kubernetes and storage/memory measurement work with reproduction repos; this week's cgroup-v2 `container_memory_working_set_bytes` piece is the best explanation of why that metric misleads for Postgres. P2. https://ardentperf.com
- **planetscale.com/blog (Engineering)** `[org]` — vendor (Postgres + Vitess host) but the engineering posts are substantive Postgres internals: Jan Nidzwetzki's MVCC/bloat deep-dive with runnable psql, planner-goes-rogue postmortems, sharding write-ups. Filter the product/Traffic-Control posts; keep the internals ones. Atom feed at planetscale.com/blog/feed.atom. P3. https://planetscale.com/blog
- **coroot.com/blog** `[org]` — infra-observability vendor; Postgres posts reproduce failure modes (e.g. "Let's Break Autovacuum") rather than listing metrics. P3. https://coroot.com/blog/
- **thebuild.com (Christophe Pettus)** `[solo]` — near-daily GUC-internals series and cross-engine planner deep-dives. P2. https://thebuild.com/blog/

## PostgreSQL development (primary, highest trust)

- **pgsql-hackers mailing list** `[pipe]` — where features are actually designed and argued. Highest signal for "what's coming". P1. https://www.postgresql.org/list/pgsql-hackers/
- **PostgreSQL commitfest** `[pipe]` — patches under review; a roadmap of near-term features. P2. https://commitfest.postgresql.org/
- **PostgreSQL git commits** `[pipe]` — ground truth for "did X actually land". Use to fact-check claims. P2. https://git.postgresql.org/gitweb/?p=postgresql.git
- **pghackers.com** `[pipe]` — AI-assisted search/explorer over the pgsql-hackers archive; trial as a faster way to triage in-window threads than the raw monthly index. P3. https://www.pghackers.com/

## Wider DBMS & distributed data

- **Andy Pavlo / CMU DB Group blog** `[solo]` — industry analysis, annual "Databases in <year>" retrospective, seminar series. P1. https://www.cs.cmu.edu/~pavlo/blog/ and https://db.cs.cmu.edu/
- **DBMS Musings (Daniel Abadi)** `[solo]` — isolation/consistency, distributed DB theory made readable. P2. http://dbmsmusings.blogspot.com/
- **Murat Demirbas — Metadata blog** `[solo]` — distributed systems & database papers, paper reviews. P2. https://muratbuffalo.blogspot.com/
- **The New Stack — Databases** `[org]` — news/trends; mixed, filter for substance. P3. https://thenewstack.io/data/
- **QuestDB blog** `[org]` — time-series engine internals and skeptical benchmarking-methodology writing; surfaced via a strong HN thread ("Lies, Damn Lies and Database Benchmarks"). P3. https://questdb.com/blog/
- **awesome-database-learning** `[pipe]` — curated internals reading list; mine for new primary sources. P3. https://github.com/pingcap/awesome-database-learning
- **blog.dave.tf (David Anderson)** `[solo]` — occasional but deep systems/columnar-format write-ups (FastLanes Unified Transport Layout). P3. https://blog.dave.tf/
- **cedardb.com/blog (Umbra/TUM lineage)** `[org]` — storage encodings, compression, vectorised execution; no sales pitch. Discovered via Lobsters /t/databases + r/databasedevelopment. P3. https://cedardb.com/blog/
- **elastic.co/search-labs/blog** `[org]` — Elastic's engineering blog; the storage/columnar posts are real engine content (Columnar Mode in 9.5), the rest is product. Worth a monthly skim for the Wider-DBMS section. P3. https://www.elastic.co/search-labs/blog

## Commercial engines (new techniques & inventions — filter marketing hard)

- **SQL Server — Microsoft engineering blogs & docs** `[org]` — "What's new" + engine internals; mine for real optimizer/storage/columnstore/Hekaton-style techniques, not feature sheets. P2. https://techcommunity.microsoft.com/category/sql-server/blog/sqlserver
- **Bob Ward / SQL Server team deep-dives** `[solo]` — internals talks and write-ups. P3. https://learn.microsoft.com/en-us/sql/
- **Oracle Optimizer blog** `[org]` — CBO internals and new optimizer features straight from the team. P2. https://blogs.oracle.com/optimizer/
- **Oracle Database Insider / Maria Colgan** `[org]` — In-Memory, new-version internals. P3. https://blogs.oracle.com/database/
- **Franck Pachot** `[solo]` — cross-engine internals (Oracle, Postgres, YugabyteDB, MongoDB); excellent technique-level comparisons. P2. https://dev.to/franckpachot
- **MySQL Server Blog / engineering** `[org]` — InnoDB, optimizer, replication internals. P3. https://dev.mysql.com/blog-archive/
- **Percona blog (MySQL/Postgres/Mongo)** `[org]` — often substantive engineering; filter the product posts. P3. https://www.percona.com/blog/
- **MariaDB Foundation blog** `[org]` — engine-level write-ups (e.g. the DuckDB storage-engine line of work); also a clean MariaDB release radar. P3. https://mariadb.org/blog/
- **modern-sql.com (Markus Winand)** `[solo]` — cross-engine SQL-standard conformance and feature comparisons. P2. https://modern-sql.com/
- **shopify.engineering** `[org]` — applied MySQL/InnoDB engineering at scale (SKIP LOCKED reservation pools, composite-PK lock counts, connection-hold-time attribution). Worth a monthly skim for the Commercial-engines section. P3. https://shopify.engineering/

## Migration experience (real-world reports — prioritise)

- **AWS Database Blog — migrations** `[org]` — Oracle/SQL Server → Postgres/Aurora war stories; technical, watch for product push. P2. https://aws.amazon.com/blogs/database/
- **Stormatics** `[org]` — incident/migration field reports. P2. https://stormatics.tech/
- **pgEdge / Crunchy / EDB migration write-ups** `[no-ledger]` — judge per-post for real lessons vs. pitch; not one outlet — key ledger rows by the post's actual domain instead (pgedge.com, crunchydata.com, enterprisedb.com; the latter two already classed above). P3.
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
- **Greengage blog** `[org]` — Greenplum-lineage Postgres MPP; ops/internals (pg_upgrade/ggupgrade, ggrebalance). Watch for MPP-on-Postgres internals. P3. https://habr.com/ru/companies/greengage/articles/

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

_Pending — class decides which quarterly-review threshold applies (solo vs. org), so these
wait on the owner rather than being guessed. Once classed, promote to the section above and
remove the line here._
- hexacluster.ai/blog (Avi Vallarapu) — benchmark-backed Postgres tuning write-ups (HammerDB TPROC-C on HOT updates / fillfactor); numbers, not checklists. Appears on Planet PostgreSQL. P3. https://hexacluster.ai/blog
- exobench.ai/blog (Alexander Ioffe) — benchmark write-ups with disclosed builds and plans; the PG19 SQL/PGQ series measures `GRAPH_TABLE` against hand-written joins and recursive CTEs on a 19beta1 build. Tool-adjacent (ExoBench) and the headlines lean clickbait, but the numbers and plans are shown. P3. https://exobench.ai/blog
- seedfa.st/blog (Mikhail Shytsko) — short, reproduced-against-a-real-version Postgres failure-mode posts (sequence-out-of-sync after a fixture load, run on 18.6 with pasted output). Appears on Planet PostgreSQL. P3. https://seedfa.st/blog
- acadia.engineering/blog (Evan Czaplicki) — Datalog-inspired relational query-language project; two substantive posts in consecutive weeks ("Rethinking Database Programming," "Solving the 1+N Query Problem"), each driving genuine cross-platform HN/Reddit debate. P3. https://acadia.engineering/blog
