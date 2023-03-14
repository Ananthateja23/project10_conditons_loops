from django.shortcuts import render

# Create your views here.
def condition1(request):
    d={'a':10,'b':20}
    return render(request,'condition1.html',context=d)
def condition2(request):
    e={'a':10,'b':20,'c':30}
    return render(request,'condition2.html',context=e)
def condition3(request):
    f={'a':100,'b':200,'c':300}
    return render(request,'condition3.html',context=f)
def loops(request):
    g={'name1':"gnapika sri",'name2':'Sashank'}
    return render(request,'loops.html',context=g)