from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from .forms import LoginForm, RegistrationForm
from .models import User


class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = RegistrationForm()
        context['login_form'] = context['form']  
        return context


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'authentication/login.html'  
    success_url = reverse_lazy('item_list')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = LoginForm()  
        return context


def custom_logout_view(request):

    logout(request)
    
    messages.success(request, "You have been successfully logged out.")
    
    return redirect('login')