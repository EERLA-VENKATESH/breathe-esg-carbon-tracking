\# TRADEOFFS.md - What Was Deliberately Not Built



\## Three Features Not Implemented



\### 1. Configurable Validation Rules Engine

\*\*Why not built\*\*: MVP assumes hardcoded validation rules per source type

\*\*What would trigger building it\*\*: Multiple clients need different validation logic (e.g., different acceptable ranges for activity values)

\*\*Workaround for now\*\*: Validation rules are in code; changes require deployment



\### 2. Bulk Review Operations

\*\*Why not built\*\*: Assignment focuses on single-record accuracy and review workflow

\*\*What would trigger building it\*\*: Analysts need to review > 100 records per day, or batch approval by date range/source

\*\*Workaround for now\*\*: Individual approve/flag/reject for each record



\### 3. Real-time API Ingestion

\*\*Why not built\*\*: All data sources provide file exports, not real-time APIs

\*\*What would trigger building it\*\*: Client needs sub-minute data freshness or has API-only sources

\*\*Workaround for now\*\*: File upload with async processing queue



\## Honorable Mentions (Considered but Rejected)

\- \*\*Machine Learning anomaly detection\*\*: Requires labeled historical data (6+ months)

\- \*\*PDF bill parsing\*\*: All sources provide CSV/structured exports

\- \*\*Blockchain audit trail\*\*: Overkill for MVP; standard DB audit log sufficient

