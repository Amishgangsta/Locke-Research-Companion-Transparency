#!/usr/bin/env python3
"""Static checks for a public-documentation-only repository; not a source or runtime audit."""
from pathlib import Path
import re,sys
root=Path(__file__).resolve().parents[1]
expected={
 'README.md','CHANGELOG.md','PUBLISHING.md',
 'docs/ASK-LOCKE-AND-SOURCES.md','docs/RESEARCH-COVERAGE.md',
 'docs/CASE-FILES-AND-EVIDENCE.md','docs/ATTORNEY-PREP.md',
 'docs/REPORTS-AND-EXPORTS.md','docs/PRIVACY-AND-SECURITY.md',
 'docs/MODELS-AND-AI-BOUNDARIES.md','docs/CLIENT-USE-CASES.md',
 'docs/FEATURE-REFERENCE.md','docs/TECHNICAL-ARCHITECTURE.md',
 'docs/VERIFICATION-AND-STATUS.md'}
problems=[]
found={str(p.relative_to(root)).replace('\\','/') for p in root.rglob('*.md')}
if expected-found: problems.append('Missing: '+', '.join(sorted(expected-found)))
for f in root.rglob('*'):
 if not f.is_file(): continue
 rel=str(f.relative_to(root)).replace('\\','/')
 if f.stat().st_size>350000: problems.append('Oversize: '+rel)
 if f.suffix.lower() in {'.ts','.tsx','.js','.jsx','.env','.pdf','.docx','.pem','.key','.db','.sql'}:problems.append('Disallowed source-type file: '+rel)
 if rel.startswith(('public/','services/','routes/','db/','libraries/','data/','middleware/')):problems.append('Private-project path: '+rel)
for p in root.rglob('*.md'):
 s=p.read_text(encoding='utf-8')
 for link in re.findall(r'\]\(([^)]+)\)',s):
  if link.startswith(('http://','https://','mailto:','#')): continue
  base=link.split('#',1)[0]
  if base and not (p.parent/base).exists():problems.append(f'{p.relative_to(root)} broken link {base}')
full='\n'.join(x.read_text(encoding='utf-8') for x in root.rglob('*.md')).lower()
for term in ['ask locke','source-backed','jurisdiction','case file','ocr','attorney','privacy','205a11c']:
 if term not in full:problems.append('Missing topic: '+term)
print(f'Checked {len(list(root.rglob("*.md")))} Markdown files; {len(problems)} issue(s).')
for p in problems:print('FAIL:',p)
sys.exit(bool(problems))
