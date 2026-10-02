#!/usr/bin/env python3
"""Check portable references, generated-file parity and public archive contents."""
from pathlib import Path
import re
import zipfile
from build_bundle import ROOT, SOURCES, archive_members, render_bundle


def main():
    errors = []
    markdown_files = sorted(p for p in ROOT.rglob('*.md') if 'dist' not in p.parts)
    link_pattern = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
    for path in markdown_files:
        body = path.read_text(encoding='utf-8')
        for target in link_pattern.findall(body):
            if target.startswith(('https://', 'http://', 'mailto:')):
                continue
            file_part, _, fragment = target.partition('#')
            resolved = (path.parent / file_part).resolve() if file_part else path
            if not resolved.exists():
                errors.append(f'{path.relative_to(ROOT)}: missing {target}')
            elif path.name == 'DAILY_LEARNING.md' and fragment:
                if f'id="{fragment}"' not in body:
                    errors.append(f'Broken bundled anchor: {fragment}')
        if re.search(r'/Users/|/private/tmp/|Hotel Management Academy', body):
            errors.append(f'Nonportable or personal path in {path.relative_to(ROOT)}')

    bundle = ROOT / 'DAILY_LEARNING.md'
    if not bundle.exists() or bundle.read_text(encoding='utf-8') != render_bundle():
        errors.append('DAILY_LEARNING.md is stale; run scripts/build_bundle.py')
    archive = ROOT / 'dist/daily-learning.zip'
    if archive.exists():
        with zipfile.ZipFile(archive) as z:
            expected = {'daily-learning/' + p.relative_to(ROOT).as_posix(): p.read_bytes()
                        for p in archive_members()}
            if set(z.namelist()) != set(expected):
                errors.append('Archive does not match public file allowlist')
            for name, content in expected.items():
                if name in z.namelist() and z.read(name) != content:
                    errors.append(f'Stale archived file: {name}')
            if z.testzip() is not None:
                errors.append('Corrupt archive')
    else:
        errors.append('Missing release archive')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(markdown_files)} Markdown files; {len(SOURCES)} bundled sources; '
          'relative links, bundle parity and archive content. External URLs and '
          'live AI/provider behavior are not tested by this script.')


if __name__ == '__main__':
    main()
