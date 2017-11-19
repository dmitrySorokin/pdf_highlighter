from pdf_highlighter import create_highlight, create_circle, create_square, create_free_text, highlight_file

annotations_dict = {
    0: [
        create_highlight(50, 740, 560, 800, color=(1, 1, 0)),
        create_square(50, 650, 500, 680),
        create_circle(50, 700, 550, 720, color=(0, 0, 0)),
        create_free_text(50, 500, 500, 600, 'This is FreeText!', color=(0, 0, 1))]}

highlight_file('data/mipt_conference.pdf', 'data/mipt_conference_out.pdf', annotations_dict)
