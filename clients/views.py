from django.shortcuts import render
from .models import Client

def index(request):
    """The main page for clients"""
    clients = Client.objects.order_by('date_added')
    context = { 'clients': clients }
    return render(request, 'index.html', context)

def client(request, client_id):
    """Show a single client"""
    client = Client.objects.get(id=client_id)
    context = { 'client': client }
    return render(request, 'client.html', context)