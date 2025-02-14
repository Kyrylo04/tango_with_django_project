from django.shortcuts import render, get_object_or_404
from rango.models import Category
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('rango:index')
    else:
        form = AuthenticationForm()
    
    return render(request, 'rango/login.html', {'form': form})


def category_detail(request, category_slug):

    category = get_object_or_404(Category, slug=category_slug)

    pages = category.page_set.all()

    context_dict = {
        'category': category,
        'pages': pages,
    }

    return render(request, 'rango/category_detail.html', context=context_dict)

def add_category(request):
    form = CategoryForm()  
    
    if request.method == 'POST':  
        form = CategoryForm(request.POST)  
        
        if form.is_valid():
            form.save(commit=True)  
            return redirect('/rango/')  
            
        else:
            print(form.errors)
            
    return render(request, 'rango/add_category.html', {'form': form})

# Logout View
def user_logout(request):
    logout(request)
    return redirect('rango:index')

# Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('rango:index')
    else:
        form = AuthenticationForm()
    return render(request, 'rango/login.html', {'form': form})

# Register View
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rango:login')
    else:
        form = UserCreationForm()
    return render(request, 'rango/register.html', {'form': form})

# Set prefence
def set_user_preference(request):
    request.session['user_preference'] = 'dark_mode'
    return render(request, 'rango/preferences.html')

# Get prefence
def get_user_preference(request):
    user_preference = request.session.get('user_preference', 'light_mode')
    return render(request, 'rango/preferences.html', {'preference': user_preference})
