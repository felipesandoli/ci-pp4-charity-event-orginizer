from django.shortcuts import render, redirect
from django.views import View, generic
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages import constant as messages
from django.urls import reverse_lazy


class HomePage(View):

    def get(self, request):
        return render(request, 'index.html')


# Signup following learndjango tutorial  
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect("homepage")