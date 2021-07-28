
# Views.py 

# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    info = {'name':'vimal','place':'Noida'}
    return render(request, 'index.html', info)



def exe1(request):
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse((sites))

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    if removepunc=="on":
         punctutaion = '''[]""':;/?.>,<!~@#$%^&*()"'''
         analyzed = " "
         for char in djtext:
             if char not in punctutaion:
                 analyzed = analyzed + char
         params = {'purpose':'Removed Puntutaion','analyzed_text':analyzed}
         djtext=analyzed
    if(fullcaps=="on"):
        analyzed=" "
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Removed Puntutaion','analyzed_text':analyzed}            
        djtext=analyzed
    
    if(newlineremover=='on'):
        analyzed=" "
        for char in djtext:
            if char !='\n' and char !='\r':
                analyzed=analyzed+char
        params = {'purpose':'Removed Puntutaion','analyzed_text':analyzed}   
        djtext=analyzed   
    if(removepunc !='on' and fullcaps !='on' and newlineremover !='on'):
        return HttpResponse("Please select atleast one choice") 
    return render(request,'analyze.html',params)
   
