# Ask Locke, research modes, and source integrity

[Back to overview](../README.md)

## Three research workflows

| Mode | Primary use | Source status |
|---|---|---|
| Quick Answer | Initial question, general explanation, short pass | Not presented as a primary-source-verified research memo |
| Source-Backed Research | Retrieve law relevant to a scoped question | Supports citation and coverage audits |
| Deep Research | Extended, multi-pass exploration of issue/authority and contrary material | Retains bounded retrieval and citation controls |

`services/research_engine.js` resolves the mode, retrieves sources for source-backed/deep work, supplies bounded source text to the model, and audits the answer against retrieved sources. All-results/provider-failure conditions are handled explicitly. The audit is a *source-match check*, not a guarantee of legal accuracy, precedential weight, current good law, or completeness.

## Jurisdiction and court selection

`services/locke_research_scope.js` resolves jurisdiction with precedence **explicit request → issue → case file → workspace**. Court selection uses **explicit request → case-file default**; an explicitly incompatible court is an error, and a stale inherited court can be reset. The resolved scope is returned for display. Uploaded evidence may be used elsewhere for jurisdiction inference, but it does not replace this canonical precedence chain without confirmation.

## Citation audit

The audit compares numbered citation markers with the actual retrieved source count and checks reporter citations, statutory-section references, and case names against source text/metadata. Source-backed research can fail closed when the audit is blocking. A passing match only means a corresponding string was found in retrieved material—not that an authority is valid, controlling, correctly interpreted, or still good law.

## Sources and limitations

CourtListener opinions and federal primary-source routes are used alongside search-derived state statutory material. The research engine caps the retrieval context: up to eight mapped sources, source snippets limited to 3,000 characters, and 24,000 combined snippet characters. A result can therefore omit relevant authority even when the search was successful. The app indicates source-coverage gaps and partial provider failures; state statutes require checking the official current code.

## Responsible model use

The application treats quoted evidence and retrieved excerpts as untrusted data in the prompt; it separates public source retrieval from private document context. Research text and selected private documents can be supplied to AI synthesis providers. Source text may be truncated by size and mode. Provider/model choice is internal to the application; no current claim is made about which commercial models are enabled in production.

**Evidence:** `services/research_engine.js`; `services/citation_audit.js`; `services/locke_research_scope.js`; `services/model_router.js`; `services/research_llm.js` at `205a11c`.
