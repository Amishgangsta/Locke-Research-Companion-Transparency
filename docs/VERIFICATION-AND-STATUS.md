# Evidence, status, and verification

[Back to overview](../README.md)

**Inspection date:** 2026-10-31. **Source repository:** private `Amishgangsta/Locke-Research-Companion-Official`. **Branch:** `main`. **Source SHA:** `205a11c90c1f05d3a6132f827258ec48b0a0e449` ("Repair durable OCR workflow", 2026-09-10). **Product website:** `https://lockeresearchcompanion.com`.

## Verified from current GitHub source

- Main SHA and source files were obtained through the connected GitHub API in this session.
- Case authorization, research scope precedence, source retrieval, citation checking, PDF/DOCX output, OCR job processing, export warnings, and model-adapter distinctions are evidenced by source modules.
- The code registers 52 public jurisdictions and separate unspecified/general scope.
- The code contains attorney-packet and report generation from labeled case evidence.
- The code contains a production release-readiness check and separate local test-auth path.

## Not independently verified this session

- The public website was unreachable to independent web inspection; no assertion is made that today's Railway deployment runs the inspected SHA or passes all production checks.
- The earlier owner-supplied count of 335 named courts was not independently recalculated and has not been adopted as a verified headline figure.
- The original README reports a prior test baseline; tests were not run during this public documentation build. No current "all tests green" claim is made.
- Provider keys, live model selections, actual customer access, provider retention terms, external security certifications and prices were not inspected.
- The source README includes historical limits that conflict with a newer catalog section using null/unlimited values for several categories; this package omits numerical quota claims.

## Source reference map

| Claim | Inspected source path |
|---|---|
| Jurisdiction and court scoping | `services/locke_research_jurisdiction.js`, `services/locke_research_courts.js`, `services/locke_research_scope.js` |
| Research modes/retrieval | `services/research_engine.js`, `services/legal_research.js` |
| Citation audit and warnings | `services/citation_audit.js`, `services/research_export_formats.js` |
| Case isolation and deletion | `services/locke_research_case_files.js`, `services/locke_research_documents.js` |
| Timeline/facts/packets/reports | `services/locke_research_companion.js` |
| OCR jobs | `services/locke_research_ocr_jobs.js`, `services/ocr_engine.js` |
| Model execution | `services/model_router.js`, `services/model_catalog.js`, `services/research_llm.js` |
| Release conditions | `services/release_readiness.js` |

The source file paths are provenance identifiers, not a redistribution of private code.
