# accounts/views.py (Custom Login View)
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('welcome_page')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid username or password!'})
    return render(request, 'registration/login.html')