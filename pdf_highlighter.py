from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import (
    DictionaryObject,
    FloatObject,
    NameObject,
    ArrayObject,
    TextStringObject,
)


# x1, y1 starts in bottom left corner
def _create_annotation(x1, y1, x2, y2, color, subtype):
    annotation = DictionaryObject()

    annotation.update({
        NameObject('/Subtype'): NameObject(subtype),
        NameObject('/C'): ArrayObject([FloatObject(c) for c in color]),
        NameObject('/Rect'): ArrayObject([
            FloatObject(x1),
            FloatObject(y1),
            FloatObject(x2),
            FloatObject(y2)]),
    })

    return annotation


def _add_annotation(annotation, page):
    if '/Annots' in page:
        page[NameObject('/Annots')].append(annotation)
    else:
        page[NameObject('/Annots')] = ArrayObject([annotation])


def create_highlight(x1, y1, x2, y2, color=(1, 0, 0)):
    return _create_annotation(x1, y1, x2, y2, color, '/Highlight')


def create_circle(x1, y1, x2, y2, color=(1, 0, 0)):
    return _create_annotation(x1, y1, x2, y2, color, '/Circle')


def create_square(x1, y1, x2, y2, color=(1, 0, 0)):
    return _create_annotation(x1, y1, x2, y2, color, '/Square')


def create_underline(x1, y1, x2, y2, color=(1, 0, 0)):
    return _create_annotation(x1, y1, x2, y2, color, '/Underline')


def create_strike_out(x1, y1, x2, y2, color=(1, 0, 0)):
    return _create_annotation(x1, y1, x2, y2, color, '/StrikeOut')


def create_free_text(x1, y1, x2, y2, text, color=(1, 0, 0)):
    annotation = _create_annotation(x1, y1, x2, y2, color, '/FreeText')
    annotation[NameObject('/Contents')] = TextStringObject(text)
    return annotation


def highlight_file(file_in, file_out, annotations_dict):
    pdf_input = PdfFileReader(open(file_in, 'rb'))
    pdf_output = PdfFileWriter()

    for page_number in range(pdf_input.getNumPages()):
        page = pdf_input.getPage(page_number)
        if page_number in annotations_dict:
            for annotation in annotations_dict[page_number]:
                _add_annotation(annotation, page)
        pdf_output.addPage(page)

    output_stream = open(file_out, 'wb')
    pdf_output.write(output_stream)
