from django.shortcuts import render


def index(request):
    """The main page for clients"""
    return render(request, 'index.html')
