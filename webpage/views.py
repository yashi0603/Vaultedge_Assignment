from django.shortcuts import render,HttpResponse
import PyPDF2

# Create your views here.
def index(request):
    return render(request, 'index.html')

def compute(request):
    
    pdfFile = request.POST.get('formFile')
    pageNo = int(request.POST.get('pageNo'))
    rotateAngle = int(request.POST.get('rotateAngle')) 
    
    inp = open(pdfFile,'rb')
    
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfWriter = PyPDF2.PdfFileWriter()
    
    page = pdfReader.getPage(pageNo).rotateCounterClockwise(rotateAngle)
    pdfWriter.addPage(page)
    
    out = open('newFile.pdf','wb')
    pdfWriter.write(out)
    
    out.close()
    inp.close()
    
    return HttpResponse("PDF FILE ROTATED page number: {}, {}degrees".format(pageNo,rotateAngle))