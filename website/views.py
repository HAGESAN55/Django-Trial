from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def beranda(request):
    return render(request, 'beranda.html')


def main(request):
    return render(request, 'index.html')
