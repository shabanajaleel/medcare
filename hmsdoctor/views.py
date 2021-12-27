from django.shortcuts import render

def fndashbord(request):
    return render(request,"docdashbord.html")

def fnheader(request):
    return render(request,"docheader.html")


