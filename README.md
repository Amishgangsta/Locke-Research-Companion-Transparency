# Locke Research Companion

### Source-aware legal research. Organized case evidence. Better-prepared conversations with counsel.

**Legal research is more useful when the answer, the authority, and the facts remain connected.** Locke Research Companion combines Ask Locke, jurisdiction-scoped legal research, document intelligence, case timelines, issues and facts, and attorney-preparation materials inside a continuing case-file workspace.

Rather than generating an answer that becomes a disconnected chat message, the product helps users collect legal questions, distinguish retrieved authorities from assertions, and carry the record forward into a professional consultation.

**[Explore Locke Research Companion](https://lockeresearchcompanion.com)** · [Research and citations](docs/ASK-LOCKE-AND-SOURCES.md) · [Case-file workflows](docs/CASE-FILES-AND-EVIDENCE.md) · [Privacy and AI boundaries](docs/PRIVACY-AND-SECURITY.md)

> **Public product and technical reference — not application source code.** Grounded in the private Locke Research Companion Official repository, branch `main`, commit `205a11c90c1f05d3a6132f827258ec48b0a0e449`, reviewed October 31, 2026. The product website was not accessible to the independent web inspection used for this documentation build; current live behavior, live pricing, and provider configuration have not been verified. The implementation repository remains private and is not redistributed.

---

## From the first question to the attorney meeting

| Research problem | Locke Research Companion capability | Why it matters |
|---|---|---|
| A quick answer lacks context | **Ask Locke** with question, jurisdiction, and court context | Work begins inside the correct legal scope |
| An AI answer cites the wrong case | **Source-backed retrieval and citation audit** | Missing or unsupported citations can be flagged or block a source-backed result |
| A case spans multiple PDFs and emails | **Case files and document intelligence** | Materials stay associated with the matter |
| The sequence of events is unclear | **Timeline and date extraction** | Dates connect back to the supporting record |
| Facts are mistaken for legal conclusions | **Separate Issues & Facts boards** | Assertions can have source text, confidence, and verification markers |
| Preparing for counsel requires reconstruction | **Attorney Prep and case reports** | Documents, events, questions, and research are assembled into a reviewable packet |
| Research needs to leave the system | **PDF and DOCX exports** | Memoranda and reporting preserve material source-coverage warnings |

## Ask Locke: three paths into research

**Quick Answer** provides a concise first pass. **Source-Backed Research** gathers legal materials and evaluates citations against the retrieved source list. **Deep Research** conducts a broader, bounded multi-pass search to build an extended analysis. These modes serve different purposes; a quick answer is not the same thing as source-backed verification.

- **Research with the scope visible.** The application resolves a jurisdiction and, when selected, a court system; explicit instructions can override inherited defaults, and an incompatible court selection is rejected or reset according to its source.
- **Use real source records.** Retrieved items retain title, citation when present, source, coverage indicator, and URL when supplied.
- **Surface citation problems.** Reporter citations, statutes, case names, and numbered markers are compared with retrieved material; source-backed responses may be rejected when citation audit fails.
- **Carry warnings forward.** Partial provider failures and search-derived state-statute limitations are disclosed; the export layer can repeat them in the research memorandum.
- **Keep matters distinct.** Case-file authorization controls which private documents can be used as context for a research request.

[**How Ask Locke, retrieval, citations and AI boundaries work**](docs/ASK-LOCKE-AND-SOURCES.md)

## U.S. legal research, with jurisdiction-aware court scoping

The source registry covers **50 states, the District of Columbia, and U.S. federal law (52 public jurisdictions)**, with maintained court-structure entries used to guide research scope. It is not a guarantee that every court opinion, law, or state code provision is available through connected retrieval sources.

The research path integrates legal-source retrieval, including CourtListener for opinions, federal legislative sources, federal regulations, and search-derived state statutory materials. **State statutory coverage can be incomplete and requires checking the current official code** before reliance.

[**Jurisdictions, retrieval sources, and known coverage limits**](docs/RESEARCH-COVERAGE.md)

## One case file; connected material

A case file anchors uploaded documents, saved research, legal issues, factual statements, significant dates, preparation packets, and reports. Users can maintain multiple cases, archive and restore matters, and initiate a confirmation-gated permanent deletion workflow.

**Document intelligence** includes PDF, DOCX, and text extraction; summaries, plain-English explanation, and attorney-question prompts; and OCR jobs for scanned PDFs, including page-by-page acceptance before finalization. A timeline may incorporate source-linked dates from documents and cross-document review. The facts board stores the statement and supporting source wording separately from legal issues.

[**Explore document, OCR, timeline, and evidence workflows**](docs/CASE-FILES-AND-EVIDENCE.md)

## Turn case materials into attorney-ready work

**Attorney Prep** composes a structured consultation packet from selected case evidence, covering key facts, dates, documents, issues requiring review, missing information, and questions for counsel. Case reports use selected evidence sections rather than relying on the case title alone; prior AI-generated research is explicitly labeled as model output, not original authority, during evidence assembly.

**Illustrative workflows:** developing an event chronology from correspondence; comparing inconsistent accounts; preparing document-specific questions for a lawyer; reviewing multiple records before a consultation; and exporting a research memorandum with coverage warnings.

[**See five practical use cases**](docs/CLIENT-USE-CASES.md) · [**Reporting and exports**](docs/REPORTS-AND-EXPORTS.md)

## Privacy-conscious design with clear boundaries

Private case materials are protected by authenticated, user-, firm-, and case-scoped access checks in the inspected application code. Legal-source search requests are designed to use the research question, while **selected private document context can be transmitted to the configured AI synthesis provider** to perform requested analysis. Scanned-PDF OCR is processed through a document-bound job workflow with acceptance controls.

Deleting a case follows a documented content-removal and storage-purge workflow; filesystem removal can require retries, and no claim is made here about external providers' retention or backup expiration without a current infrastructure assessment.

[**Read the privacy, security, and provider-boundary reference**](docs/PRIVACY-AND-SECURITY.md)

## Built for reviewable results, not autonomous legal decisions

- **Case-level evidence isolation:** the server checks ownership and the active case before retrieving private materials.
- **Visible scope and provenance:** structured jurisdiction rules, source metadata, and a citation-audit step.
- **Provider-safe processing:** retrieved content and uploaded case documents are treated as untrusted data rather than instructions.
- **Controlled AI routing:** direct OpenAI and OpenRouter adapters are implemented; other vendors may be reached through OpenRouter where supported and configured.
- **Usage accounting:** guarded research actions record attempts and usage; available features and limits depend on deployment configuration.
- **Human verification:** OCR acceptance, fact-verification indicators, citation warnings, and attorney review remain essential parts of the workflow.

[**Technical architecture**](docs/TECHNICAL-ARCHITECTURE.md) · [**Feature reference**](docs/FEATURE-REFERENCE.md) · [**Verification record**](docs/VERIFICATION-AND-STATUS.md)

---

### Product boundary

Locke Research Companion provides **legal information, source organization, document intelligence, and case preparation**. It is **not a law firm, an AI lawyer, a court service, or a substitute for legal advice**. AI-generated findings, OCR, case facts, and citations require review against the applicable authoritative materials.

**Website:** [lockeresearchcompanion.com](https://lockeresearchcompanion.com) · **Inspected revision:** `205a11c` · **Documentation review:** 2026-10-31 · **Pricing:** intentionally omitted.
