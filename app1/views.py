from django.shortcuts import render

# Create your views here.
def my(request):
    return render(request,'my.html')

def my1(request):
    return render(request,'my1.html')