from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("hello,world.you are at the index page.")
    return render(request,'pages/index.html')

def about(request):
    # return HttpResponse("this is the about page.")
     return render(request,'pages/about.html')