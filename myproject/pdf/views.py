from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from media.workingwithpdftwo import workpdf

# Create your views here.
def project(request):
    pagecontent="pagecontent"
    if request.method=='POST':
        print(request.POST)
        valuesfrom=request.POST
        #print(request.FILES)
        uploadfile=request.FILES['document']
        #print(uploadfile.name)
        #print(uploadfile.size)
        fs=FileSystemStorage()
        fs.save(uploadfile.name,uploadfile)
        pagecontent=workpdf(uploadfile.name,valuesfrom['color'],valuesfrom["fontsize"],valuesfrom["bgcolor"],valuesfrom["fontstyle"])
        print(pagecontent)
        url = fs.url(uploadfile)
        name=url.split(".")
        realname=name[0]+".pdf"
        originalfile=uploadfile.name.split(".")
        filename="/home/bhas/Desktop/djangoprojects/myproject/"+originalfile[0]+".pdf"
        context={
            "pagecontent":pagecontent,
            "filename"   :filename,
            "url"        :realname
        }
        print("yes it is working")
        return render(request,"index.html",context)
    return render(request,"index.html",{})


