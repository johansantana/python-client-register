from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import RegisterUserForm

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # display blank registration form.
        form = RegisterUserForm()
    else:
        # Process completed form.
        form = RegisterUserForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page
            login(request, new_user)
            return redirect('clients:index')

    # display a blank or invalid form
    context = {'form': form}
    return render(request, 'register.html', context)

def logout(request):
    return render(request, 'logged_out.html')
