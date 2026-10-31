# Privacy, security, and AI processing boundaries

[Back to overview](../README.md)

Legal case records require identifiable boundaries, not a broad claim that AI is private by default. The claims here concern **controls visible in the application source**, not a completed security audit or an independent assessment of the current hosting configuration.

## Access control

- JWT-backed authentication protects private research endpoints outside explicitly gated local development mode.
- Case files, documents, research history and related materials are scoped to the authenticated user's and firm's identifiers; linked evidence is checked against case ownership.
- Production setup rejects insecure placeholder JWT configuration, and local personal-test bypass is not permitted in production mode.
- Private application pages are configured as non-indexable; public methodology/jurisdiction pages are a separate surface.

## AI and third-party data boundaries

- Public legal-source retrieval is intended to receive the research question and scope, **not the uploaded private document content**.
- **Private document excerpts may be transmitted to configured LLM synthesis providers** when a user requests research, document analysis or case synthesis.
- Third-party law retrieval, provider processing, storage, logging, and deletion practices are distinct. Zero-retention, local-only inference, attorney-client privilege, and end-to-end encryption are **not claimed** by this publication.
- The research prompt contains explicit instructions to treat retrieved snippets and uploaded documents as untrusted data, not executable instructions; this is a mitigation, not proof against prompt injection.

## Document handling and removal

Supported uploads are checked for extension/MIME and configured size limits. DOCX expansion has size/ratio safeguards. Original uploads are written outside the public asset path in the configured storage location. Soft deletion hides a file and attempts storage removal. Permanent purge clears stored text and derivative records transactionally; filesystem removal has retry handling, so deletion completion must be interpreted with the returned storage-purge status. Historical backups and third-party copies are not independently audited here.

## Operational safeguards

Guarded research execution performs preflight usage checks, reservation/accounting and error handling. Persistent-volume and database configuration are required by the production release-readiness checker. Model and retrieval provider credentials are required for their respective live features.

## Unverified

Production security headers, actual provider retention terms, TLS settings, database-at-rest encryption, backup expiration, penetration testing, external compliance certifications, and the currently live deployed commit were not independently verified during this documentation build.

**Evidence:** `middleware/auth.js`; `services/locke_research_case_files.js`; `services/locke_research_documents.js`; `services/research_engine.js`; `services/release_readiness.js` at `205a11c`.
