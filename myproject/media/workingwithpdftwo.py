
from fpdf import FPDF
from PIL import Image
from .colors import colorfunc
import os
class PDF(FPDF):
    def chapter_body(self, name, colour,bgcolor, fontsize,fontstyle):
        print(name)
        #self.image("download.jpeg",95,145,0,25)
        returncolor=colorfunc(colour,"text")
        red = returncolor[0]
        green = returncolor[1]
        blue = returncolor[2]
        self.set_font('times', '', int(fontsize))
        self.set_text_color(red, green, blue)
        self.add_font('Lobsterk','',"fonts/{}".format(fontstyle),uni=True)
        self.set_font('Lobsterk', '', int(fontsize))


        #self.set_font('times', '', fontsize)
        #self.set_fill_color(0,230,0)
        #self.set_text_color(230,0,0)
        #bgred=0
        #bggreen=0
        #if bgcolor == "red":
        #    bgred=200
        #if bgcolor == "green":
        #    bggreen = 200
        #if bgcolor == "blue":
        #    bgblue = 200
        bgcolorreturn=colorfunc(bgcolor,"bg")
        bgred=bgcolorreturn[0]
        bggreen=bgcolorreturn[1]
        bgblue=bgcolorreturn[2]
        with open(name, 'rb') as fh:
            txt = fh.readlines()#.decode('latin-1')
            for line in txt:
                s=''
                for i in line:
                    print(self.get_string_width(s+chr(i)),self.w)
                    if self.get_string_width(s+chr(i))>195:
                        self.cell(0,5,s+chr(i),ln=True)
                        s=""
                    else:
                        s += chr(i)
                if s != "":
                    self.cell(0,5,s[0:-2:],ln=True)
                #self.set_fill_color(bgred,bggreen,bgblue)
                #self.set_draw_color(0,80,200)
                #print(self.w)
                #totalwords=self.w//self.get_string_width('h')
                #print(totalwords)
                #print(len(line))
                #print(type(totalwords))
                #if self.get_string_width(line.decode('latin-1')) > totalwords:
                    #i = int(totalwords)
                    #intial=0
                    #while True:
                        #self.cell(0,int(fontsize)/4+1,line.decode('latin-1')[intial:intial+i:],fill=False)
                        #self.ln()
                        #intial = intial + i
                        #if line.decode('latin-1')[intial:intial+i]=="":
                            #break
                #else:
                    #self.cell(0,int(fontsize)/4+1,line.decode('latin-1'),fill=False)
                    #self.ln()
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
def workpdf(filename, colorto, fontsize,bgcolor,fontstyle):
    pdffile = "/home/bhas/Desktop/djangoprojects/myproject/media/{}".format(filename)
    print(pdffile)
    pdf = PDF('P', 'mm', 'Letter')
    pdf.add_page()
    bgcolorreturn = colorfunc(bgcolor,"bg")
    bgred=bgcolorreturn[0]
    bggreen=bgcolorreturn[1]
    bgblue=bgcolorreturn[2]
    img = Image.new(mode="RGB",size=(400,300),color=(bgred,bggreen,bgblue))
    img.save("red.png")
    pdf.image("red.png",x=5,y=5,w=205,h=260,type='',link='')
    pdf.add_font('Lobsterk','',"fonts/{}".format(fontstyle),uni=True)
    pdf.set_font('Lobsterk', '', int(fontsize))
    #pdf.set_fill_color(250,0,250)
    pdf.chapter_body(pdffile, colorto,bgcolor,fontsize,fontstyle)
    fileorginalname=filename.split('.')
    finalname=fileorginalname[0]+".pdf"
    pdf.output(finalname)
    os.system("cp /home/bhas/Desktop/djangoprojects/myproject/{} /home/bhas/Desktop/djangoprojects/myproject/media/".format(finalname))
#workpdf(filename,"red",18)
