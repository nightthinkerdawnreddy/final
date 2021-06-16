#from django.shortcuts import render
from fpdf import FPDF
#import PyPDF2


class PDF(FPDF):
    def chapter_body(self, name, colour, fontsize):
        print(name)
        with open("/home/bhas/Desktop/djangoprojects/myproject/media/{}".format(name), 'rb') as fh:
            txt = fh.read().decode('latin-1')
        #s = "H"*23
        red = 0
        green = 0
        blue = 0
        if colour == "red":
            red = 200
        if colour == "green":
            green = 200
        self.set_font('times', '', int(fontsize))
        self.set_text_color(red, green, blue)
        print(txt)
        self.multi_cell(0, 5, txt)
        # print(self.get_string_width("H"))
        # print(self.w)
        # print(215.89999999999998/9.1694)
        self.ln()


def workpdf(filename, colorto, fontsize):
    pdffile = "/home/bhas/Desktop/djangoprojects/myproject/media/{}".format(
        filename)
    print(pdffile)
    #print(colorto,"this is working")
    # pdffile=filename
    # pdfread=PyPDF2.PdfFileReader(pdffile)
    # page=pdfread.getPage(0)
    # pagecontent=page.extractText()
    # return pagecontent
    # return render(request,"pdf.html",{"pagecontent":pagecontent})
    # workpdf("pdf4.pdf")
    #############################################################
    pdf = PDF('P', 'mm', 'Letter')
    pdf.add_page()
    pdf.chapter_body(pdffile, colorto, fontsize)
    print("executing the output")
    fileorginalname=filename.split('.')
    finalname=fileorginalname[0]+".pdf"
    pdf.output(finalname)
# workpdf("hello","red")
