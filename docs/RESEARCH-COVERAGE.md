# Jurisdiction coverage and legal research sources

[Back to overview](../README.md)

## Court-scoped research

The source registry provides 52 public jurisdiction choices: all 50 states, the District of Columbia, and the U.S. federal system. The general/unspecified selection is authenticated-only and does not appear as a public jurisdiction hub. State-specific named court hierarchies are represented in the maintained court registry, with fallback behavior designed to avoid fabricating court names.

## Source character

| Source family | Role | Important limitation |
|---|---|---|
| CourtListener | Published judicial opinions | Retrieval does not by itself establish validity, treatment, or full coverage |
| Congress.gov and federal law retrieval | Legislative materials, public laws | A proposed bill is not enacted law |
| eCFR | Federal regulations | Currency and applicability still require checking the authority |
| State statutory search | State-code discovery | Search-derived snippets may be incomplete, outdated, or secondary |

The application tracks source metadata, coverage labels, provider errors, and partial results where available. It can refuse source-backed research when all providers fail or when required statutory coverage fails. A jurisdiction page describing a hierarchy is not an endorsement by that court or a guarantee of complete searchable case law.

## Public site structure

Source files describe public methodology, jurisdiction hubs, and court directories with canonical URLs; authenticated screens are treated as non-indexable. The source README documents 107 indexable pages at its historical verification point. Independent web access was unavailable during the October 31, 2026 documentation build, so exact currently served page counts and the stated 335 named court entries are **not independently confirmed** in this release.

**Evidence:** `services/locke_research_jurisdiction.js`, `services/locke_research_courts.js`, `services/public_pages.js`, `services/research_engine.js` at `205a11c`.
