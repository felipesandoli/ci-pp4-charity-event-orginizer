from django.shortcuts import render
from django.views import View, generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class HomePage(View):

    def get(self, request):
        return render(request, 'index.html')

# Signup following learndjango tutorial  
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
    