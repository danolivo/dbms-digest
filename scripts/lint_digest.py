#!/usr/bin/env python3
"""Enforce the digest length limits from SKILL.md ("Length limits", step 9).

Usage: python3 scripts/lint_digest.py digests/YYYY-MM-DD.md
Exit status 1 if any violation is found.

Rules checked:
  * no nested list items or indented continuation lines, except under
    "## Upcoming events" (at most 3 sub-bullets per event, <=25 words each);
  * regular item: <=35 words after the headline;
  * item tagged `[release]`: <=60 words and <=3 sentences;
  * "## CommitFest" is exempt from word limits, not from nesting.
Word counts exclude the linked headline, URLs, the trailing *(author · source)*,
backtick tags, [xx] language tags, _(orig: …)_ and _[paper]_.
"""
import re
import sys

REGULAR_MAX = 35
RELEASE_MAX = 60
RELEASE_SENTENCES = 3
TALK_MAX = 25


def body_words(line):
    s = line[2:] if line.startswith('- ') else line.strip()[2:]
    # drop the linked headline(s) up to the em dash separator
    if ' — ' in s:
        s = s.split(' — ', 1)[1]
    s = re.sub(r'`[^`]*`', ' ', s)                 # `[tags]`
    s = re.sub(r'_\(orig:.*?\)_', ' ', s)          # original title
    s = re.sub(r'_\[[^\]]*\]_', ' ', s)            # _[paper]_
    s = re.sub(r'\*\([^*]*\)\*', ' ', s)           # *(author · source)*
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)  # links -> text
    s = re.sub(r'\[(ru|zh|ja|fr|de|ko|es|pt)\]', ' ', s)
    s = s.replace('**', '').replace('*', '')
    return s.split(), s


def sentences(text):
    return len(re.findall(r'[.!?](?=\s+[A-Z(`*"]|\s*$)', text.strip())) or 1


def main(path):
    errors = []
    section = ''
    talks = 0
    for n, raw in enumerate(open(path, encoding='utf-8').read().split('\n'), 1):
        line = raw.rstrip()
        if line.startswith('## '):
            section = line[3:]
            continue
        if not line.strip():
            continue
        if line.startswith((' ', '\t')):
            if section.startswith('Upcoming events') and line.lstrip().startswith('- '):
                talks += 1
                w, _ = body_words(line.lstrip())
                if talks > 3:
                    errors.append(f'{n}: more than 3 talk picks for one event')
                if len(w) > TALK_MAX:
                    errors.append(f'{n}: talk pick has {len(w)} words (max {TALK_MAX})')
                continue
            errors.append(f'{n}: nested/indented line in "{section}" — not allowed')
            continue
        if not line.startswith('- '):
            continue
        talks = 0
        if section.startswith('CommitFest') or section.startswith('New sources'):
            continue
        words, text = body_words(line)
        if '`[release]`' in line:
            if len(words) > RELEASE_MAX:
                errors.append(f'{n}: release item has {len(words)} words (max {RELEASE_MAX})')
            if sentences(text) > RELEASE_SENTENCES:
                errors.append(f'{n}: release item has {sentences(text)} sentences (max {RELEASE_SENTENCES})')
        elif len(words) > REGULAR_MAX:
            errors.append(f'{n}: item has {len(words)} words (max {REGULAR_MAX})')
    for e in errors:
        print(f'{path}:{e}')
    print(f'{len(errors)} violation(s)')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
