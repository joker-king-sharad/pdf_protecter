import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

def protect_pdf(input_file, output_file, password):
    with open(input_file, 'rb') as in_file, \
         open(output_file, 'wb') as out_file:
        input_pdf = PdfFileReader(in_file)
        output_pdf = PdfFileWriter()
        output_pdf.encrypt(password)
        for page in input_pdf.pages:
            output_pdf.addPage(page)
        output_pdf.write(out_file)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f'Usage: {sys.argv[0]} input_file output_file password')
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    password = sys.argv[3]

    protect_pdf(input_file, output_file, password)

    print('PDF file protected successfully')
