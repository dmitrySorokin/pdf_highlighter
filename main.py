from pdf_highlighter import highlight, highlight_file

highlights_dict = {
    0: [
        highlight(50, 740, 560, 800, color=(1, 0, 1)),
        highlight(50, 650, 500, 680, color=(1, 0, 0))]}

highlight_file('data/mipt_conference.pdf', 'data/mipt_conference_out.pdf', highlights_dict)
