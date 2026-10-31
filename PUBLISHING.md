# Publishing the Research Companion public reference

This package is deliberately documentation-only and intended for a **new public** GitHub repository; it is not a copy of the private application.

**Proposed repository:** `Amishgangsta/Locke-Research-Companion-Transparency`

**Suggested description:** "Source-aware legal research and case preparation: Ask Locke, verified-source workflows, case files, OCR, attorney-prep reports and privacy boundaries. Public technical reference."

## Windows PowerShell process

1. Extract the ZIP into a **new, standalone folder** named `Locke-Research-Companion-Transparency`, outside any private product checkout.
2. Install and authenticate the GitHub CLI (`gh auth status`) and make sure `git` is available.
3. From the extracted folder run `python .\scripts\verify_public_docs.py` for file and Markdown-link safety checks.
4. Run `.\scripts\Publish-Public-Repo.ps1`. The helper refuses to execute in an unexpected folder, from an existing Git repository, or against an existing GitHub target repository. It creates a new public GitHub repository containing **only this folder's files**.
5. Open the new public README and inspect its links. Review product claims again before using them as current sales representations.

The current ChatGPT GitHub connector can update existing repositories but does **not** provide repository creation. This package is not published to GitHub automatically.

## Explicit boundaries

- Never change the private implementation repository's visibility.
- Never publish `.env`, database files, credentials, prompts, original legal templates, customer data or implementation code.
- Publishing these public docs does not change the Railway deployment or the live website.
- Update status claims only after a new source and runtime verification pass.
