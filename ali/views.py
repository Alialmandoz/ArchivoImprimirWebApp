from django.shortcuts import render


def home(request):
    return render(request, 'ali/home.html')


def work(request):
    return render(request, 'ali/work.html')


def contact(request):
    return render(request, 'ali/contact.html')


def about(request):
    return render(request, 'ali/about_me.html')