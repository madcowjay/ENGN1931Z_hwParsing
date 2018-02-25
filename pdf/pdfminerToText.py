# Following code from https://www.binpress.com/tutorial/manipulating-pdfs-with-python/167
# Tim Arnold article on "Manipulating PDFs from Python)

# Using PDFMiner.six

import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def convert(fname, pages=None):
    if not pages:   
        pagenums = set()
    else:
        pagenums = set(pages)
    output = io.StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, codec='utf-8', laparams=LAParams())
    infile = open(fname, 'rb')
    interpreter = PDFPageInterpreter(manager, converter)
    for page in PDFPage.get_pages(infile, pagenums, maxpages=0,
                                  password="",
                                  caching=True,
                                  check_extractable=True):
        interpreter.process_page(page)
    text = output.getvalue()
    infile.close()
    converter.close()
    output.close()
    return text

# Note: For alternative implementations, see http://stackoverflow.com/questions/26494211/extracting-text-from-a-pdf-file-using-pdfminer-in-python/
