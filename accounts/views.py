# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth.models import User


from .forms import SignUpForm

def signup(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            
            return redirect('home')
    else :
        form = SignUpForm()


    context = {
        'form':form,
    }
    return render(request, "signup.html", context)


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name','email',)
    template_name= 'my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user
     