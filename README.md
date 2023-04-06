# merge_pdfs
simple script for merging multiple PDF files in one

## dependencies 
pip install PyPDF2
pip install pyinstaller

use "pyinstaller --onefile --windowed --additional-hooks-dir=. merge_pdfs.py" to generate an executable

## use
merge_pdfs.exe input_pdf1.pdf input_pdf2.pdf ... output_pdf.pdf
