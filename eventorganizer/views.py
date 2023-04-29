from django.shortcuts import render, redirect
from django.views import View, generic
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm


class HomePage(generic.ListView):
    model = Event
    queryset = Event.objects.filter(approved=True, archived=False)
    paginate_by = 16
    template_name = 'index.html'


# Signup following learndjango tutorial
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"


class Logout(View):

    def get(self, request):
        logout(request)
        messages.add_message(
            request, messages.SUCCESS, "You have been successfully logged out"
        )
        return redirect("homepage")


class CreateEvent(View):

    def get(self, request, *args, **kwargs):
        event_form = EventForm()
        return render(
            request, "event_form.html", {"event_form": event_form})

    def post(self, request, *args, **kwargs):
        event_form = EventForm(request.POST)

        if event_form.is_valid():
            event_form.instance.owner = request.user
            event_form.save()
            messages.add_message(
                request, messages.SUCCESS, "Your event has been created and is now pending approval."
            )
            return redirect("homepage")
        else:
            messages.add_message(
                request, messages.ERROR, "Something went wrong. Please try again"
            )
            event_form = EventForm()
            return render(
                request, "event_form.html", {"event_form": event_form}
            )
