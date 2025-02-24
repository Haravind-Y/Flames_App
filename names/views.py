from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'base.html')


def answer(request):
    a=request.POST['n1']
    b=request.POST['n2']
    a=a.lower().replace(' ','')
    b=b.lower().replace(' ','')
    for i in a:
        for j in b:
            if i==j:
                a=a.replace(i,'',1)
                b=b.replace(j,'',1)
                break
    result=len(a+b)
   
    flames=['Friends','Lovers','Attraction','marriage','Enemy','Sibling'] 
    while len(flames)>1:
        index=result % len(flames)-1
        if index<0:
            flames=flames[:-1]   
        else:
            right=flames[index+1:]
            left=flames[:index]   
            flames= right +left   
    return render(request,"result.html",{'result':flames[0]})   


