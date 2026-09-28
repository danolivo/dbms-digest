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
  exactly the reader's wheelhouse — but **link discovery only, not Community pulse** (2026-09-21: 3 posts
  in the window, **0 comments on all three**; second consecutive week with no debate). `[js]`
  https://www.reddit.com/r/databasedevelopment/ . P1 for discovery, skip for the pulse.
- **r/SQL** — broader SQL Q&A and discussion; filter heavily. `[js]`
  https://www.reddit.com/r/SQL/top/?t=week . P2.
- **r/Database** — general DB talk; smaller, noisier. `[js]`
  https://www.reddit.com/r/Database/top/?t=week . P3.
- **r/dataengineering** — pipelines/warehouses; lots of vendor noise, occasional gold. `[js]`
  https://www.reddit.com/r/dataengineering/top/?t=week . P3.
- **r/vectordatabase** — small, but the most active vector-DB-specific forum found so far; practitioner
  comparison chatter that never reaches HN. `[js]` https://old.reddit.com/r/vectordatabase/ . P3.
- **r/mariadb** — effectively an official channel: the MariaDB Foundation posts its monthly newsletter
  and community polls there. Low volume, high signal per post. `[js]` https://old.reddit.com/r/mariadb/ . P3.
- **r/DuckDB** — steady on-topic posting, low comment counts; a discovery feed rather than a discussion
  source. `[js]` https://old.reddit.com/r/DuckDB/ . P3.
- **r/ClickHouse** — 3.6k subscribers but consistently on-topic practitioner chatter (ingestion patterns,
  Postgres↔ClickHouse), and the only place ClickHouse discussion is visible outside HN. `[js]`
  https://old.reddit.com/r/ClickHouse/ . P3.
- **r/MySQL** — 49k subscribers; thin weeks are normal, but the list otherwise covers MariaDB and has no
  MySQL-proper community at all. `[js]` https://old.reddit.com/r/MySQL/ . P3.

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
- **MariaDB Foundation Zulip — `general`** — **publicly readable without login** (verified 2026-09-14 by
  reading a day's traffic). A live feed of MariaDB/InnoDB *development* — MDEV tickets, force-pushed PRs,
  JIRA bot filings — which is the register this digest wants and which no subreddit provides. Only a
  subset of channels is browsable logged-out; `general`, `Buildbot`, `JIRA` and `GitHub - MariaDB Server`
  are. `[js]` https://mariadb.zulipchat.com/#narrow/channel/118759-general . P2.
- **`t.me/clickhouse_ru`** — 11,237 members, clearly the most active Russian-language ClickHouse venue,
  but it is a **group, not a channel**: `t.me/s/` redirects to the join page, so content is unreadable
  without membership. `[auth]` — listed so it is not re-discovered every run. Never fabricate its
  content. P-.
- **#postgresql on Libera.Chat (IRC)** — public channel, but no reliable public web archive.
  `[auth]` (effectively). P-.
- **Public Telegram channels** — readable without login via the web preview
  `https://t.me/s/<channel>`. None pinned yet — **discover and add** the ones worth following
  (English and Russian-language Postgres/DBMS channels). `[public]` once a channel is named. P2.

---

## Discovery log

_Real source finds only — access technique lives in references/fetching.md instead. Cap: 15
most-recent entries; older ones roll off (git history has the rest)._
- (2026-06-20) _seed list created._
- hntoplinks.com — week/month views of top HN stories with live points/comments; a scan aid, not a primary source, for when HN's own listing pages are cache-stale. `[public]` P2. https://www.hntoplinks.com/week
- hckrnews.com — chronological HN front-page mirror with points/comments; covers only the most recent ~2–3 days, useful for the tail of the week. `[public]` P3. https://hckrnews.com/
- (2026-09-07) r/vectordatabase, r/mariadb, r/DuckDB added to the weekly sweep — see Forums above.
- (2026-09-07) **Caveat learned this run:** several of the highest-comment r/SQL threads in a week can
  share a template (lowercase philosophical title, "Postgres 15, X downstream" framing, abstract hook),
  one author, and accounts registered the day they post. The *comments* are real practitioners. Report
  the discussion, never attribute the framing to "the community."
- acadia.engineering (Evan Czaplicki's Datalog-flavored query-language project) — also a recurring Community-pulse driver (its posts have twice driven the week's biggest r/programming or HN database thread); listed as a publisher in sources.md, cross-referenced here.
- (2026-09-14) r/ClickHouse and r/MySQL added to the weekly sweep; **MariaDB Foundation Zulip** added as the
  first genuinely readable development-chat source (see Chat & messengers).
- (2026-09-14) **Access notes worth keeping:** `api.stackexchange.com` is CORS-blocked from a `lobste.rs`
  origin despite being CORS-open generally — navigate a tab directly to the API URL and parse
  `document.body.innerText`. `t.me/s/<channel>` is CORS-blocked from any other origin and must be loaded
  as a page. `lobste.rs/t/databases.json` returns the tag feed as JSON with `score`, `comment_count` and
  `created_at` — cleaner than scraping `a.u-url`.
- (2026-09-14) **Telegram searches keep returning aggregators, not sources.** `t.me/sqlhub` (36k subs) is a
  cross-promotion channel whose bio is a list of other channels; its top post that week was a game ad.
  Rejected on the anti-marketing filter — do not add.
- (2026-09-21) **Two more Telegram candidates rejected on the same `t.me/s/` test:** `t.me/pgsql` (13,792
  members, 1,912 online — large and clearly active, but a *group*, so `t.me/s/` renders only the
  description) and its English sibling `t.me/pg_sql`; `t.me/pgdaily` exists but has had zero posts since
  2024-02-24. Not scrapeable / not alive — do not re-discover.
- (2026-09-21) **DBA SE watch-tag `polardb`:** six PolarDB/IMCI questions landed 09-14→09-20 (IDs 350768,
  350769, 350771, 350775, 350777, 350778), all from 21–31-reputation accounts, all zero answers. Reads as
  a seeding campaign rather than organic traffic — track the tag precisely so it can be filtered out.
- (2026-09-21) **Reddit access note:** batching subreddit `.json` calls with `credentials:'omit'` fails
  wholesale ("Failed to fetch"); same-origin relative-path fetches with a ~900 ms gap between them work.

- (2026-09-28) **r/databasedevelopment went silent** — zero posts in the Sep 21–27 window (third thin week running). Keep for discovery one more month; retire if October stays empty.

## Retired (removed from weekly scan)

_When a source goes dead/dormant/promotional, move it here with date + reason so it isn't
re-added by mistake. Populated by the quarterly source review in SKILL.md ("Keeping the skill
healthy") once an outlet reaches `[dormant]`, or immediately when a source is confirmed
dead/gone outside that cycle._
- **(2026-09-14) r/CockroachDB** — zero posts in the trailing week; `top.json?t=week` returned an empty
  listing. Dormant; dropped from the sweep.
- **(2026-09-14) r/dbt** — zero posts in the trailing week. Dormant; dropped from the sweep.
- **(2026-09-14) `t.me/tantorlabs`** — created 2022-11-11, **2 subscribers, zero posts ever**. Recorded so
  it is not "discovered" again.
- **(2026-09-14) Checked, too quiet to justify a weekly slot (not retired, just not added):** r/sqlite
  (11 posts/week, max 7 comments), r/cassandra (2 posts all week), r/mongodb (5 posts, max 5 comments).
