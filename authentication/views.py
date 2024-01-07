from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from . import forms
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from car.models import Car
# Create your views here.

class RegisterUser(CreateView):
    model = User
    form_class = forms.RegistrationForm
    template_name = "register.html"
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Register'
        return context

class UserLoginView(LoginView):
    template_name='register.html'

    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        return context

@login_required
def profile(request):
    cars = Car.objects.filter(buyer=request.user)
    return render(request, 'profile.html', {'cars':cars})

@method_decorator(login_required, name='dispatch')
class EditProfile(UpdateView):
    model = User
    form_class = forms.ChangeUserForm
    template_name = 'update_profile.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy("profile")

def user_logout(request):
    logout(request)
    return redirect('login')