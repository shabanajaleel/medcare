from django.shortcuts import render

def Home(request):
    return render(request,'index.html')

def Homehead(request):    
    return render(request,'home.html',)

def fndepart(request):
    return render(request,'depview.html')
