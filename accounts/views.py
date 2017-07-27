from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    """
    User Registration View "Sign Up"    
 
    """
    if request.method == "GET":
        form = CustomUserCreationForm()

    elif request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False) #checks that the form fields are correctly completed
            #We can make any last second changes to the user.
            user.save() #saves the user to the database
            return redirect('/accounts/login') #this redirects you to the page you are now allowing the user to see

    context = {'form': form}
    return render(request, 'registration/register.html', context)

def login(request):
    """Logs the user in."""

    if request.method == "GET":
        form = AuthenticationForm()

    #Step 1 -> Handle POST
    elif request.method == "POST":
        #Step 2 -> Get Form Data
        username = request.POST.get('username')
        password = request.POST.get('password')
        #Step 3 -> Validate Form Data
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #Step 4 -> Check Username & Password (Authenticate)
            user = authenticate(username=username, password=password)
            if user:

                #Step 5 -> LogIn (Session)
                django_login(request, user)
                #Step 6 -> Redirect
                return redirect('calendar_view')

    context = {'form': form}
    return render(request, 'registration/login.html', context)

def logout(request):
    django_logout(request)
    # messages.info(request, 'You have logged out.')
    return redirect('/')