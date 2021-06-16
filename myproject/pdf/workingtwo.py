import PyPDF2
file=open("/home/bhas/Desktop/djangoprojects/myproject/pdf_1.pdf","rb")
reader=PyPDF2.PdfFileReader(file)
print(reader.getPage(0).extractText())
