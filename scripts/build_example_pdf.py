#!/usr/bin/env python3
"""Render the public sample. Developer dependency: reportlab (not needed by readers)."""
from pathlib import Path
from html import escape
import re
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted

ROOT = Path(__file__).resolve().parents[1]


def inline(value):
    value = escape(value)
    value = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',
                   r'<a href="\2" color="#137C83"><u>\1</u></a>', value)
    value = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', value)
    return re.sub(r'`([^`]+)`', r'<font name="Courier">\1</font>', value)


def main():
    source = ROOT / 'examples/python/preview.md'
    destination = source.with_suffix('.pdf')
    base = ParagraphStyle('body', fontName='Helvetica', fontSize=10.5,
                          leading=14.5, spaceAfter=7, textColor=colors.HexColor('#233B44'))
    title = ParagraphStyle('title', parent=base, fontName='Helvetica-Bold',
                           fontSize=26, leading=30, spaceAfter=12)
    heading = ParagraphStyle('heading', parent=base, fontName='Helvetica-Bold',
                             fontSize=13.5, leading=17, spaceBefore=9, spaceAfter=6,
                             keepWithNext=True)
    item = ParagraphStyle('item', parent=base, leftIndent=10, spaceAfter=4)
    code = ParagraphStyle('code', fontName='Courier', fontSize=9.4, leading=13,
                          backColor=colors.HexColor('#F0F6F6'), borderPadding=9,
                          spaceBefore=5, spaceAfter=12, alignment=TA_LEFT)
    story = []
    paragraph = []
    code_lines = []
    fenced = False

    def flush():
        if paragraph:
            story.append(Paragraph(inline(' '.join(paragraph)), base))
            paragraph.clear()

    for line in source.read_text(encoding='utf-8').splitlines():
        if line.startswith('```'):
            flush()
            if fenced:
                story.append(Preformatted('\n'.join(code_lines), code))
                code_lines.clear()
            fenced = not fenced
        elif fenced:
            code_lines.append(line)
        elif not line.strip():
            flush()
        elif line.startswith('# '):
            flush()
            story.append(Paragraph(inline(line[2:]), title))
        elif line.startswith('## '):
            flush()
            if line == '## Practice':
                story.append(PageBreak())
            story.append(Paragraph(inline(line[3:]), heading))
        elif re.match(r'^\d+\. ', line):
            flush()
            story.append(Paragraph(inline(line), item))
        else:
            paragraph.append(line)
    flush()
    if fenced:
        raise ValueError('Unclosed code block')

    def page(canvas, doc):
        width, height = A4
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor('#137C83'))
        canvas.setLineWidth(2)
        canvas.line(44, height-29, width-44, height-29)
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(colors.HexColor('#587078'))
        canvas.drawString(44, 25, 'DAILY LEARNING  /  PUBLIC SAMPLE  /  WRITTEN-SOURCE FALLBACK')
        canvas.drawRightString(width-44, 25, str(doc.page))
        canvas.restoreState()

    doc = SimpleDocTemplate(str(destination), pagesize=A4, rightMargin=44,
                            leftMargin=44, topMargin=44, bottomMargin=43,
                            title='Daily Learning - One list, two names',
                            author='Daily Learning')
    doc.build(story, onFirstPage=page, onLaterPages=page)
    print(destination)


if __name__ == '__main__':
    main()
