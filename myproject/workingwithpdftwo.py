
from fpdf import FPDF
from PIL import Image
class PDF(FPDF):
    def chapter_body(self, name, colour="red", fontsize=1):
        print(name)
        #self.set_font('times', '', fontsize)
            #pdf.add_font('Lobster',r"/home/Desktop/djangoprojects/myproject/Lobster-Regular.ttf",uni=True)
        self.image("download.jpeg",10,10,0,25)
        #self.set_fill_color(255,255,255)
        self.set_text_color(230,0,0)
        with open(name, 'rb') as fh:
            txt = fh.readlines()#.decode('latin-1')
            for line in txt:
                #self.set_fill_color(bgred,bggreen,bgblue)
                #self.set_draw_color(0,80,200)
                #length = 0
                s=''
                for i in line:
                    print(self.get_string_width(s+chr(i)),self.w)
                    if self.get_string_width(s+chr(i))>190:
                        self.cell(0,5,s+chr(i),ln=True)
                        s=""
                    else:
                        s += chr(i)
                if s != "":
                    self.cell(0,5,s,ln=True)
                #self.set_fill_color(230,0,230)
                #self.set_draw_color(0,80,200)
                #totalwords=self.w//self.get_string_width('h')
                #print(type(totalwords))
                #if self.get_string_width(line.decode('latin-1')) > totalwords:
                #    i = int(totalwords)
                #    intial=0
                #    while True:
                #       self.cell(0,fontsize/4+1,line.decode('latin-1')[intial:intial+i:])
                #        self.ln()
                #        intial = intial + i
                #        if line.decode('latin-1')[intial:intial+i]=="":
                #            break
                #else:
                #    self.cell(0,3,line.decode('latin-1'))
                #   self.ln()
        #print(self.w)
        #print(self.get_string_width('h'))
        #print(self.w/self.get_string_width('h'))
        #red = 0
        #green = 0
        #blue = 0
        #if colour == "red":
        #    red = 200
        #if colour == "green":
        #    green = 200
        #self.set_font('times', '', int(fontsize))
        #self.set_text_color(red, green, blue)
        #print(txt)
        #self.multi_cell(0, 5, txt)
        #self.ln()
def workpdf(filename, colorto, fontsize):
    pdffile = "/home/bhas/Desktop/djangoprojects/myproject/media/first.txt"
    print(pdffile)
    pdf = PDF('P', 'mm', 'Letter')
    pdf.add_page()
    img = Image.new(mode="RGB",size=(400,300),color=(0,255,0))
    img.save("red.png")
    pdf.image("red.png",x=10,y=10,w=195,h=260,type='',link='')
    #pdf.set_fill_color(250,0,250)
    pdf.add_font('Lobster',"","Lobster-Regular.ttf",uni=True)
    pdf.set_font('Lobster', '', fontsize)
    #pdf.set_font('Lobster','',fontsize)
    pdf.chapter_body(pdffile, colorto, fontsize)
    print("executing the output")
    pdf.output("pdf5.pdf")
workpdf(filename+".pdf","red",18)
