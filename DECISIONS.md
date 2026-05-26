\# DECISIONS.md - Key Architectural Decisions



\## 1. JSONField for Raw Data Storage

\*\*Decision\*\*: Use JSONField to store original raw\_data

\*\*Rationale\*\*: Each source (SAP, UTILITY, TRAVEL) has different schemas. JSON preserves all original fields for complete audit trail.



\## 2. Separate Raw and Normalized Tables

\*\*Decision\*\*: Keep RawEmissionRecord and NormalizedEmissionRecord as separate tables

\*\*Rationale\*\*: Maintains source-of-truth; allows re-normalization if emission factors or rules change; supports debugging.



\## 3. DecimalField for Emissions Calculations

\*\*Decision\*\*: Use DecimalField instead of FloatField

\*\*Rationale\*\*: Regulatory carbon reporting requires exact precision. Float can introduce rounding errors.



\## 4. Foreign Key for Organization Everywhere

\*\*Decision\*\*: All tables have organization foreign key

\*\*Rationale\*\*: Multi-tenancy - data must never mix between organizations, even in analytics.



\## Questions to Ask the PM

\- Should one raw\_record ever produce multiple normalized\_records? (e.g., fuel split across scopes)

\- What is the SLA for review queue? (24 hours, 48 hours, 5 days?)

\- Can analysts manually override calculated\_emissions, or only approve/reject?

\- Which emission factor database should be default? (DEFRA, EPA, IPCC?)

