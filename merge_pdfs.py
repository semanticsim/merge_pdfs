import sys
import PyPDF2


def merge_pdfs(pdfs, output):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf in pdfs:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)
    print(f"PDFs merged into {output}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python merge_pdfs.py <pdf1> <pdf2> ... <output.pdf>")
        sys.exit(1)

    pdf_files = sys.argv[1:-1]
    output_pdf = sys.argv[-1]

    merge_pdfs(pdf_files, output_pdf)
