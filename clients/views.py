from django.shortcuts import render, redirect

from .models import Client
from .forms import ClientForm


def index(request):
    """The main page for clients"""
    clients = Client.objects.order_by('date_added')
    context = { 'clients': clients }
    return render(request, 'index.html', context)

def new_client(request):
    """Add a new client"""
    if request.method != 'POST':
        # No data submitted
        form = ClientForm()
    else:
        # POST data submitted
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients:index')
        
    # Display a blank or invalid form
    context = { 'form': form }
    return render(request, 'new_client.html', context)


def edit_client(request, client_id):
    """Edit an existing client"""
    client = Client.objects.get(id=client_id)

    if request.method != 'POST':
        # Initial request
        form = ClientForm(instance=client)
    else: 
        # POST data submitted
        form = ClientForm(instance=client, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients:index')
        
    context = { 'client': client, 'form': form }
    return render(request, 'edit_client.html', context)