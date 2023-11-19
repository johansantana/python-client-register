from django.shortcuts import render
from .models import Client

def index(request):
    """The main page for clients"""
    clients = Client.objects.order_by('date_added')
    context = { 'clients': clients }
    return render(request, 'index.html', context)
