# pdf_split.py 

from PyPDF2 import PdfFileReader, PdfFileWriter

def split(path, start_page, end_page, output):
    pdf_reader = PdfFileReader(path)
    pdf_writer = PdfFileWriter()

    for page in range(start_page-1,end_page):
        pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
        
    print("Done!")

if __name__ == '__main__':
    print('Drag PDF to split below')
    pdf_input = input()
    print('Enter start page')
    start = input()
    print('Enter end page')
    end = input()
    print('Enter output PDF file name with extension')
    output_name = input()
    print('Extracting page ' + start + ' to ' + end)
    split(pdf_input, int(start), int(end), output_name)
    # path = 'RowanCounty_FIS.pdf'
    # split(path, 18, 30, 'Rowan_FIS_SOD.pdf')
