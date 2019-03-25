from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
# Create your views here.
    
def signup(req):
    if req.method == "POST" :
        form = forms.SignupForm(req.POST)
        if form.is_valid():
            user = form.save()
            auth_login(req,user)            
            return redirect('boards-home')
    else :
        form = forms.SignupForm()
    return render(req,"signup.html",{'form': form})
