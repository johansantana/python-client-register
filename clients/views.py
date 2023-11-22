from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Client
from .forms import ClientForm

@login_required
def index(request):
    """The main page for clients"""
    clients = Client.objects.filter(user=request.user).order_by('date_added')
    context = { 'clients': clients }
    return render(request, 'index.html', context)

@login_required
def new_client(request):
    """Add a new client"""
    if request.method != 'POST':
        # No data submitted
        form = ClientForm()
    else:
        # POST data submitted
        form = ClientForm(request.POST)
        if form.is_valid():
            new_client = form.save(commit=False)
            new_client.user = request.user
            new_client.save()
            return redirect('clients:index')
        
    # Display a blank or invalid form
    context = { 'form': form }
    return render(request, 'new_client.html', context)


@login_required
def edit_client(request, client_id):
    """Edit an existing client"""
    client = Client.objects.get(id=client_id)
    if client.user != request.user:
        raise Http404


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

@login_required
def delete_client(request, client_id):
    """Delete an existing client"""
    client = Client.objects.get(id=client_id)
    if client.user != request.user:
        raise Http404
    
    client.delete()
    return redirect('clients:index')