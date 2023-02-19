from PyPDF2 import PdfMerger
import os
from PDFmodule import PDF

if __name__ == '__main__':

    instancePDF = PDF(['merged_file.pdf', 'merger.pdf', 'merger2.pdf'])
    instancePDF.joinPDF()
    instancePDF.deleteInputPDFFiles()