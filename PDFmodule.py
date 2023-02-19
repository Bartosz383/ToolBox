from PyPDF2 import PdfMerger
import os

class PDF():
    def __init__(self, pdf_files):
        self.pdf_files = pdf_files

    def joinPDF(self):

        pdf_merger = PdfMerger()

        for pdf in self.pdf_files:
            pdf_merger.append(pdf)

        pdf_merger.write('okurwa3.pdf')
        pdf_merger.close()

    def deleteInputPDFFiles(self):
        # delete files
        for pdf in self.pdf_files:
            os.remove(pdf)