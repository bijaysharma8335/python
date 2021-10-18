from PyPDF2 import PdfFileReader,PdfFileWriter
file_path="hello.pdf"
pdf = PdfFileReader(file_path)

with open("opentext.txt",'w') as f:
    for page_num in range(pdf.numPages):
        
