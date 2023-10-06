from urllib.request import Request
from django.shortcuts import render



def index(request):
    return render(request,'templatesWeb/index.html')

def implementos(request):
    return render(request, 'templatesWeb/implementos.html')

def ropa(request):
    return render(request,'templatesWeb/ropa.html')


def accesorios(request):
    return render(request,'templatesWeb/accesorios.html')



