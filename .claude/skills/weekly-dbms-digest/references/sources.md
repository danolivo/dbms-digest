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
- **pganalyze "5mins of Postgres"** `[solo]` — was a weekly walkthrough of interesting Postgres content from the prior 7 days; effectively a pre-filtered digest, and for months the most reliable single blog-discovery aid here. `[dormant]` — confirmed 2026-09-14: the series has ended. Rebranded to the "Postgres in Production" deep-dive series (Parts 2–6, May→Aug 2026); newest dated post is still 2026-08-13 and no weekly episode landed in September, which is the condition the previous entry set for this call. `pganalyze.com/blog/rss.xml` now 404s — the feed URL needs rediscovering if the main blog is kept. **The weekly scan has lost its best fan-out aid**: step 2's direct blog sweep and step 6 discovery now carry that load. Demoted P1→P3 for the blog itself. https://pganalyze.com/blog
- **PostgreSQL News Archive** `[pipe]` — official project announcements (releases, CVEs). P1. https://www.postgresql.org/about/newsarchive/
- **Hacker News (front page, db filter)** `[pipe]` — sample for database/systems threads with real discussion. P2. https://hn.algolia.com/?query=postgres

## PostgreSQL blogs (primary)

- **Bruce Momjian** `[solo]` — core team; internals, community direction. P2. https://momjian.us/main/blogs/
- **Crunchy Data blog** `[org]` — frequently substantive engineering (e.g. Elizabeth Christensen, Craig Kerstiens). Judge per-post; skip the pure product posts. **Slowing (2026-09-21): newest post 2026-09-02, and the site footer's privacy link now points at snowflake.com — the Postgres engineering output has largely moved to the Snowflake engineering blog (see below).** P3. https://www.crunchydata.com/blog
- **snowflake.com — engineering, Open Source** `[org]` — where the ex-Crunchy Postgres writing landed post-acquisition (Elizabeth Garrett Christensen's Tom Lane interview, the PG19 release-status pieces). Filter the Core Platform / Gen AI categories out; the Open Source category is the Postgres one. Added 2026-09-21. P2. https://www.snowflake.com/en/blog/engineering/
- **commandprompt.com/blog (Joshua Drake)** `[solo]` — publishes a **weekly commit-level ledger** of REL_19_STABLE and master (commit counts, revert counts, the closing commit hash) plus real release notes for pgColumnar. The cheapest way to fact-check any "PG19 lost feature X" claim; best find of the 2026-09-21 run. No RSS (the `/blog/rss.xml` URL 404s, 2026-10-05) — read `/blog.md` or the HTML index. P2. https://www.commandprompt.com/blog/
- **markwkm.blogspot.com (Mark Wong)** `[solo]` — TPC-E / DBT-5 benchmark work with published harnesses and result repositories (scale-factor sweeps on EC2). Appears on Planet but was never pinned here. Added 2026-09-21. P3. https://markwkm.blogspot.com/
- **vondra.me (Tomas Vondra)** `[solo]` — committer's own blog; low volume, but the posts are measurement-led (28 years of pgsql-hackers/commit-activity charts). Added 2026-09-21. P2. https://vondra.me/
- **hdombrovskaya.wordpress.com (Henrietta Dombrovskaya)** `[solo]` — low volume; the `pg_acm` author. Watch. Added 2026-09-21. P3. https://hdombrovskaya.wordpress.com/
- **pganalyze blog** `[org]` — query performance, planner, internals. P2. https://pganalyze.com/blog
- **EDB blog** `[org]` — enterprise Postgres, HA, migrations; filter heavily for marketing. P3. https://www.enterprisedb.com/blog
- **Timescale blog** `[org]` — time-series / analytics on Postgres; good patterns, watch for product push. P3. https://www.timescale.com/blog
- **Fujitsu (Fastware) Postgres blog** `[org]` — internals and feature deep-dives. P3. https://www.postgresql.fastware.com/blog
- **Microsoft Azure for PostgreSQL blog** `[org]` — sometimes solid internals; filter marketing. P3. https://techcommunity.microsoft.com/category/azuredatabases/blog/adforpostgresql
- **Postgres.ai blog** `[dormant]` `[solo]` — DBLab, database branching, performance tooling. Confirmed 2026-09-14: nothing since **2026-04-08**, five months. P3. https://postgres.ai/blog
- **PgDog blog (Lev Kokotov)** `[solo]` — pooler/sharding internals from the implementer; strong first-party rationale posts. P3. https://pgdog.dev/blog
- **boringsql.com (Radim Marek)** `[solo]` — reproducible Postgres internals deep-dives. P3 `[prio-unset]`. https://boringsql.com/
- **justatheory.com (David Wheeler)** `[solo]` — PGXN/extensions + Postgres↔ClickHouse interop. P3 `[prio-unset]`. https://justatheory.com/
- **event-driven.io (Oskar Dudycz)** `[solo]` — event sourcing / Postgres-as-event-store engineering. P3. https://event-driven.io/
- **pduzc.com (Zhang Chen)** `[solo]` — PostgreSQL data-recovery / file-forensics field reports (ransomware carve-out recovery, single-file-per-relation risk analysis); rare hands-on content, appears on Planet PostgreSQL. P3. https://pduzc.com/blog
- **launchbylunch.com (Sehrope Sarkuni)** `[solo]` — pgjdbc maintainer's blog; primary source for the new pg-java JVM driver (repo under the pgjdbc org). P3. https://launchbylunch.com/
- **vvka-141.github.io/pgmi/articles/ (Alexey Evlampiev)** `[solo]` — schema-migration mechanics: lock queues, transaction boundaries, `CREATE INDEX CONCURRENTLY`'s two different refusals. Tool-adjacent (pgmi) but the reasoning is about Postgres. **Caveat (2026-09-14): none of the nine articles carries a publication date anywhere on the index or the article pages**, so this source cannot be placed in a week’s window — it is effectively unusable for a dated digest until that changes. P3. https://vvka-141.github.io/pgmi/articles/
- **byteofdev.com (Jacob Jackson)** `[solo]` — occasional but high-effort systems stunts (this week: an LLM behind the Postgres wire protocol, with real storage APIs underneath). Sample, don't subscribe blindly. P3. https://byteofdev.com/
- **malisper.me (Michael Malis)** `[solo]` — the pgrust series: Postgres reimplemented in Rust, with per-optimisation measurements and disclosed benchmark setups (Volcano → batching → operator fusion → SIMD, each timed). Headline multipliers are self-reported; the engineering is first-rate. Surfaced only via live HN Algolia, not via Planet or any newsletter. P2. https://malisper.me/
- **brandur.org/fragments (Brandur Leach)** `[solo]` — short, high-signal Postgres-in-production fragments (pgtestdb template cloning). P3. https://brandur.org/
- **mehmetince.net (Mehmet Ince)** `[solo]` — vulnerability-researcher blog running a six-part "Systemic Risks in the Managed PostgreSQL Industry" series (part 1: a PostGIS memory-corruption chain to privilege escalation at Neon/Supabase/Xata). Rare first-hand Postgres-ecosystem security content; treat forward-looking 0-day claims as unverified until published. P3. https://mehmetince.net/
- **ardentperf.com (Jeremy Schneider)** `[solo]` — Postgres-on-Kubernetes and storage/memory measurement work with reproduction repos; this week's cgroup-v2 `container_memory_working_set_bytes` piece is the best explanation of why that metric misleads for Postgres. P2. https://ardentperf.com
- **planetscale.com/blog (Engineering)** `[org]` — vendor (Postgres + Vitess host) but the engineering posts are substantive Postgres internals: Jan Nidzwetzki's MVCC/bloat deep-dive with runnable psql, planner-goes-rogue postmortems, sharding write-ups. Filter the product/Traffic-Control posts; keep the internals ones. Atom feed at planetscale.com/blog/feed.atom. P3. https://planetscale.com/blog
- **coroot.com/blog** `[org]` — infra-observability vendor; Postgres posts reproduce failure modes (e.g. "Let's Break Autovacuum") rather than listing metrics. P3. https://coroot.com/blog/
- **thebuild.com (Christophe Pettus)** `[solo]` — near-daily GUC-internals series and cross-engine planner deep-dives. P2. https://thebuild.com/blog/
- **tapoueh.org (Dimitri Fontaine)** `[solo]` — infrequent but long-form, with every claim verified against a real build; the "Getting Ready for PostgreSQL 19" survey independently reproduced four of the five design problems behind the MERGE/SPLIT PARTITION revert. P2. https://tapoueh.org/blog/
- **richyen.com (Richard Yen)** `[solo]` — catalog archaeology and version-portability tooling (pg-catalog-almanac: a `pg_catalog` diff across 9.6→19); original datasets, no product attached. P3. https://richyen.com/

## PostgreSQL development (primary, highest trust)

- **pgsql-hackers mailing list** `[pipe]` — where features are actually designed and argued. Highest signal for "what's coming". P1. https://www.postgresql.org/list/pgsql-hackers/
- **PostgreSQL commitfest** `[pipe]` — patches under review; a roadmap of near-term features. P2. https://commitfest.postgresql.org/
- **PostgreSQL git commits** `[pipe]` — ground truth for "did X actually land". Use to fact-check claims. P2. https://git.postgresql.org/gitweb/?p=postgresql.git
- **pghackers.com** `[pipe]` — AI-assisted search/explorer over the pgsql-hackers archive; trial as a faster way to triage in-window threads than the raw monthly index. P3. https://www.pghackers.com/

## Wider DBMS & distributed data

- **Andy Pavlo / CMU DB Group blog** `[solo]` — industry analysis, annual "Databases in <year>" retrospective, seminar series. **Demoted P1→P3 2026-09-21:** newest post is 2026-01-04 ("Databases in 2025"), and db.cs.cmu.edu's newest news item is 2026-05-15 — this is effectively an annual publication, not a weekly one. P3. https://www.cs.cmu.edu/~pavlo/blog/ and https://db.cs.cmu.edu/
- **clickhouse.com/blog** `[org]` — Gülçin Yıldırım Jelínek and Sai Srirampur publish real Postgres-adjacent engineering here (physical-WAL-to-ClickHouse replication with architecture + benchmarks). Heavy product mix; filtered watch. Added 2026-09-21. P3. https://clickhouse.com/blog
- **DBMS Musings (Daniel Abadi)** `[dormant]` `[solo]` — isolation/consistency, distributed DB theory made readable. Confirmed 2026-09-14: newest post is **2021-03-25**, five years silent. Dropped from the weekly scan; kept here so it is not re-added. P3. http://dbmsmusings.blogspot.com/
- **Murat Demirbas — Metadata blog** `[solo]` — distributed systems & database papers, paper reviews. **Moved (confirmed 2026-10-05):** now publishes at muratdemirbas.substack.com (feed `/feed`); the blogspot address is the old archive. P2. https://muratdemirbas.substack.com/
- **The New Stack — Databases** `[org]` — news/trends; mixed, filter for substance. P3. https://thenewstack.io/data/
- **QuestDB blog** `[org]` — time-series engine internals and skeptical benchmarking-methodology writing; surfaced via a strong HN thread ("Lies, Damn Lies and Database Benchmarks"). P3. https://questdb.com/blog/
- **awesome-database-learning** `[pipe]` — curated internals reading list; mine for new primary sources. P3. https://github.com/pingcap/awesome-database-learning
- **blog.dave.tf (David Anderson)** `[solo]` — occasional but deep systems/columnar-format write-ups (FastLanes Unified Transport Layout). P3. https://blog.dave.tf/
- **cedardb.com/blog (Umbra/TUM lineage)** `[org]` — storage encodings, compression, vectorised execution; no sales pitch. Discovered via Lobsters /t/databases + r/databasedevelopment. P3. https://cedardb.com/blog/
- **elastic.co/search-labs/blog** `[org]` — Elastic's engineering blog; the storage/columnar posts are real engine content (Columnar Mode in 9.5), the rest is product. Worth a monthly skim for the Wider-DBMS section. P3. https://www.elastic.co/search-labs/blog

## Commercial engines (new techniques & inventions — filter marketing hard)

- **SQL Server — Microsoft engineering blogs & docs** `[org]` — "What's new" + engine internals; mine for real optimizer/storage/columnstore/Hekaton-style techniques, not feature sheets. P2. https://techcommunity.microsoft.com/category/sql-server/blog/sqlserver
- **Bob Ward / SQL Server team deep-dives** `[solo]` — internals talks and write-ups. P3. https://learn.microsoft.com/en-us/sql/
- **Oracle Optimizer blog** `[org]` — CBO internals and new optimizer features straight from the team. Checked 2026-09-14: newest post **2026-05-06**, four months quiet — the team has essentially stopped publishing. Still worth a monthly look because the content is first-party when it comes; demoted P2→P3. https://blogs.oracle.com/optimizer/
- **Oracle Database Insider / Maria Colgan** `[org]` — In-Memory, new-version internals. P3. https://blogs.oracle.com/database/
- **Franck Pachot** `[solo]` — cross-engine internals (Oracle, Postgres, YugabyteDB, MongoDB); excellent technique-level comparisons. P2. https://dev.to/franckpachot
- **MySQL Server Blog / engineering** `[org]` — `[dormant]` — confirmed 2026-09-07: last post 2025-03-06, and the page now redirects readers elsewhere. Use **blogs.oracle.com/mysql** `[org]` (RSS https://blogs.oracle.com/mysql/rss) instead. P3. https://dev.mysql.com/blog-archive/
- **Percona blog (MySQL/Postgres/Mongo)** `[org]` — often substantive engineering; filter the product posts. P3. https://www.percona.com/blog/
- **MariaDB Foundation blog** `[org]` — engine-level write-ups (e.g. the DuckDB storage-engine line of work); also a clean MariaDB release radar. P3. https://mariadb.org/blog/
- **modern-sql.com (Markus Winand)** `[solo]` — cross-engine SQL-standard conformance and feature comparisons. Site is alive (the feature-support matrix was current to 2026-09-01) but `/blog` **404s** and no blog index or feed URL has been located — so the outlet cannot currently be window-filtered. **Open: find the real index/feed URL.** P2. https://modern-sql.com/
- **shopify.engineering** `[org]` — applied MySQL/InnoDB engineering at scale (SKIP LOCKED reservation pools, composite-PK lock counts, connection-hold-time attribution). Worth a monthly skim for the Commercial-engines section. Index is at the site root — `/blog` 404s (corrected 2026-09-14). P3. https://shopify.engineering/

## Migration experience (real-world reports — prioritise)

- **AWS Database Blog — migrations** `[org]` — Oracle/SQL Server → Postgres/Aurora war stories; technical, watch for product push. P2. https://aws.amazon.com/blogs/database/
- **Stormatics** `[org]` — incident/migration field reports. **Access correction 2026-09-21:** the `/our-blogs` index is a dead archive (newest entry July 2024); real posts live at `stormatics.tech/blogs/<slug>` and a plain fetch of an article returns an empty body — render it in a browser. P2. https://stormatics.tech/
- **fljd.in (Florent Jardin, Dalibo)** `[solo]` — Oracle→Postgres migration mechanics from one of the three authors of PostgreSQL Migrator; writes in FR with an `/en/` mirror. Added 2026-09-21. P3. https://fljd.in/en/
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
- **tidb.net (TiDB 社区)** `[pipe]` — the TiDB user-community blog (redirects to pingkai.cn). Heavily padded with certification diaries and 架构选型 solution pages, but the tuning post-mortems and index deep-dives are real and dated. Currently the most reliably *readable* Chinese DB source — mine it, don't subscribe. **Access correction 2026-09-21: browser only** — plain fetch of `pingkai.cn/tidbcommunity/blog` returns an empty body. Authors worth following: **拍脑袋小助手**, **TiDBer_wangwenjing** (both `[solo]`, reproducible lab write-ups with version/topology/SQL); the "TiDB官方" account is pure PR. P3. https://tidb.net/blog
- **OceanBase** `[org]` — distributed DB engineering write-ups (CN). Use the community blog https://open.oceanbase.com/blog (最新 sort; browser only, renders after a few seconds). 2026-10-05: in-window output was all AgentBase product posts. P3. https://open.oceanbase.com/blog
- **Alibaba Cloud developer (PolarDB / AnalyticDB)** `[pipe]` — engine internals; huge, filter hard. `[js]` P3. https://developer.aliyun.com/
- **modb.pro (墨天轮)** `[dormant]` `[pipe]` — Chinese DBA community and articles. **Retired from the weekly scan 2026-09-14 after a third consecutive failure to enumerate it**: the page loads (title 控制台 - 墨天轮) but every listing view is a client-rendered shell from which no dated article list can be extracted, even in a real browser. Not dead as a site — unusable as a source. Do not re-add without a working enumeration path (untried: its XHR endpoints, `m.modb.pro`). https://www.modb.pro/
- **老冯云数 / blog.vonng.com (Ruohang Feng, Pigsty)** `[solo]` — high-signal PG-ecosystem essays, several per week; EN mirrors at /en/. Watch for Pigsty self-promo, the engineering is real. P2. https://blog.vonng.com/

### French `[fr]`
- **Dalibo blog** `[org]` — French Postgres consultancy; substantive internals (FR, some EN). P2. https://blog.dalibo.com/ · RSS https://blog.dalibo.com/feed.xml
- **dbi-services blog** `[org]` — Swiss; PG/Oracle/SQL Server ops (FR + EN). P3. https://www.dbi-services.com/blog/

### German `[de]`
- **Cybertec (DE)** `[org]` — `[dormant]` — confirmed gone 2026-09-07: `/de/` returns 200 but redirects to `/en/`, and both `/de/postgresql-blog-de/` and `/de/category/blog-de/` 404. No German-language Cybertec blog exists any more; use the EN edition. Do not re-add. https://www.cybertec-postgresql.com/de/
- **heise online — Datenbanken / PostgreSQL topic pages** `[org]` — **the `[de]` gap is closed (2026-09-14).** Edited German IT press with a live database beat: server-rendered, dated via `<time datetime>`, enumerable with a plain fetch. Mix of product news (drop it) and genuine `hintergrund` features (keep) — some behind the heise+ paywall. P2. https://www.heise.de/thema/Datenbanken · https://www.heise.de/thema/PostgreSQL
- _Also checked and rejected for `[de]`: **credativ.de/blog** redirects to `/en/blog/` (German edition retired, same failure mode as Cybertec DE) and the English blog is itself stale, newest post 2026-07-17; **dbi-services** publishes in English despite the Swiss base._

### Japanese `[ja]`
- **Qiita — PostgreSQL tag** `[pipe]` — large JP dev community; how-tos and internals. `[js]` P3. https://qiita.com/tags/postgresql · RSS https://qiita.com/tags/postgresql/feed
- **SRA OSS (JP) — «pgsql-hackersウォッチ»** `[org]` — a monthly pgsql-hackers digest written by a Postgres contributor (Yugo Nagata); the single most useful non-English source for tracking upstream discussion, and it lands in the first week of each month. The rest of the site is minor-version release notes. **URL corrected 2026-09-14**: `/tech-blog/postgresql-development-trends/` 404s; the posts live under the **PostgreSQL開発動向** category on the tech-blog index. Cadence confirmed — it lands ~4th–7th of the month, so it normally falls in the *first* week’s digest. P2. https://www.sraoss.co.jp/tech-blog/
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
- seedfa.st/blog (Mikhail Shytsko) — short, reproduced-against-a-real-version Postgres failure-mode posts (sequence-out-of-sync after a fixture load on 18.6; the USERSET `statement_timeout` kill-switch escape, with the cancel timed at 2.060s). Appears on Planet PostgreSQL. Second published item in a month. P3. https://seedfa.st/blog
- acadia.engineering/blog (Evan Czaplicki) — Datalog-inspired relational query-language project; two substantive posts in consecutive weeks ("Rethinking Database Programming," "Solving the 1+N Query Problem"), each driving genuine cross-platform HN/Reddit debate. **2026-09-21: could not be reached this run — the URL needs re-confirming before the next sweep. Note it is NOT `acadia.io`, which is an unrelated retail-media marketing agency.** P3. https://acadia.engineering/blog

_Added 2026-09-14, classed on entry:_
- **valkey.io/blog** `[org]` — the Valkey project’s own blog; the "Technical Deep Dive" category is actually technical (cluster-wide big-key discovery without offline RDB parsing) and it publishes roughly weekly. Fills a Redis-lineage gap the list had entirely open. P3. https://valkey.io/blog/
- **vyruss.org (Jimmy Angelakos)** `[solo]` — Postgres backup internals from someone rebuilding the tooling in Go after pgBackRest lost corporate backing and the maintainer archived the repo in April 2026. Low volume; worth a standing watch as that story develops. P3. https://vyruss.org/blog/
- **tigerdata.com/blog** `[org]` — the ex-Timescale blog, publishing plain Postgres-internals material again under the Tiger Data name (WAL write amplification measured with `pg_stat_wal`, table bloat). **Caveat:** several posts carry an agency byline ("NanoHertz Communications") rather than a named engineer, and the tail of each is a funnel — check the method every time, and cite the post’s own measured numbers rather than its conclusion. P3. https://www.tigerdata.com/blog
- **blog.pgxn.org (David E. Wheeler)** `[solo]` — PGXN development log; low volume, high signal on extension *distribution* infrastructure (doc/image link resolution, reindexing). Where Wheeler’s output moved after justatheory.com went quiet. P3. https://blog.pgxn.org/
- **heise.de Datenbanken / PostgreSQL** `[org]` — see the German section above; promoted straight in rather than parked here, because it closes a gap that had been open for weeks.

_Added 2026-09-21, classed on entry (all promoted straight into the sections above):_ commandprompt.com/blog `[solo]`, snowflake.com engineering `[org]`, markwkm.blogspot.com `[solo]`, vondra.me `[solo]`, clickhouse.com/blog `[org]`, hdombrovskaya.wordpress.com `[solo]`, fljd.in `[solo]`.
- **babel.postgresql.org** `[pipe]` — not a news source: the PostgreSQL NLS translation-status dashboard. Standing reference for translation/community items (it is the primary artefact behind the zh_CN catalog story of 2026-09-14). P3. https://babel.postgresql.org/

_Added 2026-09-28, classed on entry:_
- **pgstef.github.io (Stefan Fercot)** `[solo]` — pgBackRest failure modes reproduced end to end on real multi-node setups (archive_mode on a promoted standby). Appears on Planet. P3. https://pgstef.github.io/
- **now-next.nl/en/insights (Chris van Eijk)** `[solo]` — measured multi-tenant Postgres series (indexes, gapless per-tenant numbering, RLS, partitioning) benchmarked on PG17; several posts per week — publish only the measured ones, the index/overview posts are thin. P3. https://now-next.nl/en/insights/
- **emptysqua.re (A. Jesse Jiryu Davis)** `[solo]` — DB-research paper reviews and TLA+ writing; pairs with Murat Demirbas. P3. https://emptysqua.re/blog/
- **dbos.dev/blog** `[org]` — Postgres postmortems from a durable-execution engine built on it (SELECT DISTINCT scaling, MVCC delete locality); product mix, judge per post. P3. https://www.dbos.dev/blog
- **SOFTPOINT on Habr («Записки оптимизатора 1С»)** `[org]` — 20+ parts of measured 1C-on-PostgreSQL work (Huge Pages, memory, parallelism) with perf counters; last section of each post plugs their monitoring product. Reached via the Habr hub, so ledger rows key to the hub. P3. https://habr.com/ru/companies/softpoint/articles/
- _Access notes (2026-09-28):_ **Murat Demirbas** now publishes at **muratdemirbas.substack.com** (the 2026-09-23 review was found there, not on muratbuffalo.blogspot.com) — confirm and move the entry's URL next run. **tapoueh.org/blog/** index 404s (GitHub Pages); posts live at `/blog/YYYY/MM/<slug>/` and are on Planet. vondra.me and tapoueh.org article bodies come back empty to plain fetch — take text from Planet's page or the real browser.

_Added 2026-10-05, classed on entry:_
- **thegresqlpost.org (Vik Fearing)** `[solo]` — SQL-standard and relational-theory essays from a standard-committee member, with real Postgres history (hints, `OFFSET 0`, pg_plan_advice). About one essay a month. Feed https://thegresqlpost.org/rss.xml. P2. https://thegresqlpost.org/
- **deferworks.org** `[solo]` — query optimisation from the papers (six-part join-ordering series: DPccp → DPhyp → CD-E), with Rust code; author is a tpchgen-rs maintainer. Feed https://deferworks.org/rss.xml. P3. https://deferworks.org/
- **paradedb.com/blog** `[org]` — search-in-Postgres internals (postings layout in Postgres pages, MAXSCORE); vendor, judge per post. No feed found yet. P3. https://www.paradedb.com/blog
- **lwn.net** `[org]` — edited coverage of Postgres–kernel work and community process; paywalled for a week, subscriber links surface on HN. No DB-only feed. P3. https://lwn.net/
- **duckdb.org** `[org]` — engine-team posts; release posts carry full fix lists. Feed https://duckdb.org/feed.xml. P2. https://duckdb.org/news/
- **qiita.com/asahide** `[solo]` [ja] — measured AWS-database write-ups (version, ACU, data size stated). Feed https://qiita.com/asahide/feed `[unverified feed URL]`. P3. https://qiita.com/asahide
- _Classes resolved for ledger outlets seen this run (not promoted to the scan list):_ trigger.dev `[org]`, turbopuffer.com `[org]`, turso.tech `[org]`, supabase.com `[org]`, embracethered.com `[solo]`, bolna.ai `[org]`, cortexridge.com `[org]`, people.planetpostgresql.org/devrim `[solo]`, neon.com `[org]`, databricks.com `[org]`, oliverdb.ai `[org]`, weavori.com `[org]`, infoq.com `[org]`, barddoo.com `[solo]`, pgedge.com `[org]`.
