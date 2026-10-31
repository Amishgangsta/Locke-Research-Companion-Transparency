# AI model routing and accountable outputs

[Back to overview](../README.md)

## Provider catalog versus executable adapters

The source catalog includes names from OpenAI, Google Gemini, Perplexity, xAI Grok, DeepSeek, and Mistral. **This is not six direct integrations.** `services/model_router.js` identifies the implemented synthesis adapters as **OpenAI direct** and **OpenRouter**. Other vendor models may be reached through qualified OpenRouter slugs when the selected model, credentials and deployment route support them.

The live configuration is intentionally not represented as a fixed lineup of brands or model versions. The provider/model used for a request can depend on route, environment overrides, credentials and available model endpoints. There is no guarantee that every catalog entry is usable at any moment.

## Where AI participates

AI can help draft research explanations, summarize documents, extract candidate facts and dates, assemble packets, and synthesize selected case evidence. Those outputs must be inspected. Documents and external retrieved text are data, not authority to instruct the assistant; citation audit and evidence labeling are separate checks.

## What AI does not certify

No model determines whether an allegation is true, a citation is good law, a court hierarchy is complete, or a recommended position is legally sound. Human review, legal-source confirmation and qualified counsel remain required for legal decisions.

**Evidence:** `services/model_catalog.js`; `services/model_router.js`; `services/research_llm.js`; `services/research_engine.js`; `services/locke_research_companion.js` at `205a11c`.
