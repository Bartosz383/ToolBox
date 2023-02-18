from PyPDF2 import PdfMerger
import os

pdf_files = ['1.pdf', '2.pdf', '3.pdf']

pdf_merger = PdfMerger()

for pdf in pdf_files:
    pdf_merger.append(pdf)

pdf_merger.write('merger2.pdf')
pdf_merger.close()

# delete files
for pdf in pdf_files:
    os.remove(pdf)
