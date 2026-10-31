# Attorney preparation and case synthesis

[Back to overview](../README.md)

A first meeting with counsel is more productive when the factual chronology, documents, research and open legal questions are readily accessible. Locke Research Companion generates an attorney-preparation packet from selected case-file evidence, not an invented narrative based only on the case title.

## Packet sections

The inspected generation path requests a short summary, key facts, important dates, important documents, questions for an attorney, missing information, matters needing legal review, and research notes. The user can choose which evidence categories to include, and generated sections explicitly acknowledge when supporting case evidence is absent.

## Evidence ordering and treatment

The backend bundles case metadata, document summaries/excerpts, timeline events, legal issues, facts, and prior research under labeled sections. Prior AI research is marked **PRIOR_MODEL_OUTPUT**, not as original authority. Document excerpts are bounded to manage context length. These safeguards improve traceability but do not guarantee the model's output is complete or fully supported.

## Final review

Before sharing a packet, confirm dates, names, document quotations, source references and unresolved issues. Counsel determines legal claims and strategy; the packet is preparation material, not an attorney-client opinion.

**Evidence:** `services/locke_research_companion.js` (`buildCaseEvidenceBundle`, `generateAttorneyPrepPacket`) at `205a11c`.
