from django.shortcuts import render, redirect
from .forms import userForm 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required 

@login_required(login_url='signin')
def home(request): 
    return render(request, 'base.html')


def signup(request): 
    if request.user.is_authenticated:  
        return redirect('home_page') 
    
    if request.method == 'POST': 
        form = userForm(request.POST) 
        if form.is_valid():
            form.save() 
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password1'] 
            
            user = authenticate(request, username = username, email = email, password  = password) 
            if user is not None: 
                login(request, user) 
                return redirect('home_page') 
    else: 
        form = userForm() 
    return render(request, 'auth/signup.html', {'form': form})

 

def signin(request):
    error = None
    if request.user.is_authenticated:
        return redirect('home_page')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            error = 'Invalid credentials. Please try again.'
    
    return render(request, 'auth/signin.html', {'error': error})


def signout(request):
    logout(request) 
    return redirect('signin')

