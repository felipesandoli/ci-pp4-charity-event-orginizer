from django.shortcuts import render, redirect
from django.views import View, generic
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm


class HomePage(View):

    def get(self, request):
        queryset = Event.objects.filter(approved=True)
        return render(
            request,
            'index.html',
            {
                "queryset": queryset
            }
        )


# Signup following learndjango tutorial  
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"


class Logout(View):

    def get(self, request):
        logout(request)
        messages.add_message(request, messages.SUCCESS, "You have been successfully logged out")
        return redirect("homepage")
    

class CreateEvent(View):
    
    def get(self, request, *args, **kwargs):
        event_form = EventForm()
        return render(
            request, "event_form.html", {"event_form": event_form})
