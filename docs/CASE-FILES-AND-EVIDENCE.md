# Case files and document evidence

[Back to overview](../README.md)

## Case files organize the matter

The product provides case-file creation, default case selection, editing, archiving, restoration, and confirmation-gated permanent deletion. Research actions, documents, timeline events, issues, facts, packets and reports use server-checked case ownership and links where applicable. A shared legacy workspace is retained as a compatibility container but is not used alone to select private prompt documents.

## Documents

A user can upload a supported PDF, DOCX, or text file, then request a summary, explanation, date extraction, issue/fact identification, or attorney questions. The original file and extracted text are associated with the document record. Text density is checked when extracting PDF content; pages without usable text are candidates for OCR.

### Reviewable OCR

Scanned-PDF work is represented by durable OCR jobs that record status and page-level processing. Jobs are constrained to the authorized document and tenant, use claim leases, reservations, bounded retries, and a review/acceptance stage. The application supports accepting recognized page text and finalizing reviewed results. OCR is not a substitute for the original scanned page when accuracy matters.

## Timeline

Timeline records include dated events, optional time, source document or research links, confidence and verification flags. The application supports generating candidate dates from documents and building a chronology across multiple sources, with review needed before treating generated entries as established facts.

## Issues and facts

Issues track the legal question, description, jurisdiction, priority and status. Facts keep the assertion, cited wording, confidence, verification status and links to documents/events/issues where supplied. This separation is important: a disputed allegation remains an assertion even if it is included in a report.

## Deletion boundaries

Case deletion requires an archived case and title confirmation. The implementation uses data erasure and file-purge operations, with separately retryable filesystem removal. Reported success and external retention should not be conflated. See [privacy and security](PRIVACY-AND-SECURITY.md).

**Evidence:** `services/locke_research_case_files.js`; `services/locke_research_documents.js`; `services/locke_research_ocr_jobs.js`; `services/locke_research_companion.js` at `205a11c`.
