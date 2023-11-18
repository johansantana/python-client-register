from django.shortcuts import render


def index(request):
    """The home page for clients"""
    return render(request, 'index.html')
