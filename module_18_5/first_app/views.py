from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from . forms import RegisterForm,ChangeFromData
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.
def home(request):
    return render(request,'./home.html')

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request,"Account Created Successfully")
                form.save()
                return redirect('user_login')
        else:
            form = forms.RegisterForm
        return render(request, 'register.html', {'form' : form, 'type' : 'Register'})
    else:
        return redirect('profile')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username=name,password=userpass)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged In Successfully")
                return redirect("profile")
        else:
            messages.warning(request,"Login informtion incorrect")
            return redirect("user_login")
    else:
        form = AuthenticationForm()
        return render(request, 'register.html', {'form' : form, 'type' : 'Login'})
    
def profile(request):
    return render(request,'./profile.html')

def user_logout(request):
    logout(request)
    messages.success(request,"Logout In Successfully")
    return redirect('user_login')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request,'./passchange.html',{'form': form})
    else:
        return redirect('user_login')