# International query list (for the polyglot-search `web_search` tool)

Drives the digest's **non-English discovery** step. Each run, call the
`web_search` MCP tool (from the **polyglot-search** plugin) once per target
language below, with `freshness="week"`, then filter for marketing and
fact-check survivors against the original-language source before including
them in the `## International` section.

**Minimum every run:** ru + zh + ja + one of fr/de. Pull more when time allows.
Query in the **native language** — translate the topic, not just the keyword.
Combine a base term (below) with a rotating topic (`internals`, `replication`,
`planner/optimizer`, `vacuum`, `partitioning`, `performance`, `migration`).

Tool call shape:
`web_search(query=<native query>, language=<code>, region=<code>, freshness="week", max_results=15)`

| Lang | `language` | `region`(s) | Base query terms (native) |
|------|-----------|-------------|----------------------------|
| Russian   | `ru` | `RU`            | `PostgreSQL база данных`, `СУБД внутреннее устройство`, `оптимизатор запросов` |
| Chinese   | `zh` | `TW`, `HK`, `SG`, then `CN` | `PostgreSQL 数据库`, `数据库 内核`, `查询优化器`, `逻辑复制` (Simplified) / `資料庫`, `查詢優化` (Traditional) |
| Japanese  | `ja` | `JP`            | `PostgreSQL 内部`, `データベース 設計`, `クエリプランナ`, `レプリケーション` |
| French    | `fr` | `FR`            | `PostgreSQL base de données`, `optimiseur de requêtes`, `réplication logique` |
| German    | `de` | `DE`            | `PostgreSQL Datenbank`, `Abfrageoptimierer`, `Replikation interna` |
| Spanish   | `es` | `ES`, `MX`, `AR`| `PostgreSQL base de datos`, `optimizador de consultas`, `replicación lógica` |
| Portuguese| `pt` | `BR`            | `PostgreSQL banco de dados`, `otimizador de consultas`, `replicação` |
| Korean    | `ko` | `KR`            | `PostgreSQL 데이터베이스`, `쿼리 플래너`, `복제` |

## Chinese: reach the diaspora, not just the mainland

The polyglot-search backends run outside the Great Firewall, so they index
overseas/Traditional-Chinese blogs (Taipei, Hong Kong, Singapore, Vancouver)
that a mainland-only view would miss. Run `region="TW"` (and optionally
`HK`/`SG`) for Traditional/diaspora content **and** `region="CN"` for
Simplified/mainland — they surface different authors. Note the query-term
column has separate Simplified vs Traditional forms; use the form matching the
region. Full articles on JS-heavy mainland aggregators (modb.pro, PolarDB,
PingCAP CN) may still need the in-browser reader — this step finds the URLs.

## If the tool is unavailable

If `search_status` reports no backend (no API key configured), skip this step,
fall back to the native RSS/Atom feeds in `feeds.opml` + the Claude-in-Chrome
browser, and say so in the digest footer. Never fabricate non-English items.
