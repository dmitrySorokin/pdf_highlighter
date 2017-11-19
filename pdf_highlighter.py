from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import (
    DictionaryObject,
    FloatObject,
    NameObject,
    ArrayObject,
)


# x1, y1 starts in bottom left corner
def highlight(x1, y1, x2, y2, color=(1, 0, 0)):
    highlight = DictionaryObject()

    highlight.update({
        NameObject("/Subtype"): NameObject("/Highlight"),
        NameObject("/C"): ArrayObject([FloatObject(c) for c in color]),
        NameObject("/Rect"): ArrayObject([
            FloatObject(x1),
            FloatObject(y1),
            FloatObject(x2),
            FloatObject(y2)
        ]),
    })

    return highlight


def _add_highlight(highlight, page):
    if "/Annots" in page:
        page[NameObject("/Annots")].append(highlight)
    else:
        page[NameObject("/Annots")] = ArrayObject([highlight])


def highlight_file(file_in, file_out, highlights_dict):
    pdf_input = PdfFileReader(open(file_in, "rb"))
    pdf_output = PdfFileWriter()

    for page_number in highlights_dict:
        page = pdf_input.getPage(page_number)
        for h in highlights_dict[page_number]:
            _add_highlight(h, page)
        pdf_output.addPage(page)

    output_stream = open(file_out, "wb")
    pdf_output.write(output_stream)
