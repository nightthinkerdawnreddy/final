from fpdf import FPDF
#import fonts
# f=open('docker.txt','r')
# data=f.readlines()
# print(data)
pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()
pdf.add_font('Lobsterk', '', "fonts/Allura-Regular.ttf", uni=True)
pdf.set_font('Lobsterk', '', 16)
pdf.cell(80, 10, 'Goodbye World')
pdf.output('pdf_3.pdf')
