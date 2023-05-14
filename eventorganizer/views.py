from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy, reverse
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

    def get(self, request):
        if request.user.is_authenticated:
            event_form = EventForm()
            new_event = True
            return render(
                request,
                "event_form.html",
                {"event_form": event_form, "new_event": new_event}
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "You need to be logged in to create an event."
            )
            return redirect("login")

    def post(self, request):
        event_form = EventForm(request.POST, request.FILES)

        if event_form.is_valid():
            event_form.instance.owner = request.user
            event_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your event has been created and is now pending approval."
            )
            return redirect("homepage")
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Something went wrong. Please try again"
            )
            event_form = EventForm()
            return render(
                request, "event_form.html", {"event_form": event_form}
            )


class EventInformation(View):

    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)

        if (
            request.user.is_authenticated
            and event.approved
            and not event.archived
        ):
            return render(request, "event_information.html", {"event": event})
        elif not request.user.is_authenticated:
            messages.add_message(
                request,
                messages.ERROR,
                'You need to be logged in to see this event'
            )
            return redirect('login')
        elif not event.approved:
            messages.add_message(
                request,
                messages.ERROR,
                'The event you are trying to see is pending approval'
            )
            return redirect('homepage')
        elif event.archived:
            messages.add_message(
                request,
                messages.ERROR,
                'The event you are trying to '
                + 'see has been archived and is no longer available'
            )
            return redirect('homepage')


class EditEvent(View):

    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        event_form = EventForm(instance=event)
        new_event = False

        if request.user == event.owner:
            return render(
                request,
                "event_form.html",
                {"event_form": event_form, "new_event": new_event}
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "You cannot edit an event you do not own."
            )
            return redirect("homepage")

    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        event_form = EventForm(instance=event)
        event_form = EventForm(request.POST, request.FILES, instance=event)

        if event_form.is_valid:
            event_form.instance.approved = False
            event_form.instance.owner = request.user
            event_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your event has been updated and is now awaiting approval."
            )

            return redirect("homepage")


class DeleteEvent(View):

    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        return render(request, 'delete_event.html', {'event': event})

    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        event.delete()
        return redirect("homepage")


class JoinEvent(View):

    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        event.participants.add(request.user)
        event.save()
        return redirect(reverse('event_information', args=[event_id]))


class LeaveEvent(View):

    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        event.participants.remove(request.user)
        event.save()
        return redirect(reverse('event_information', args=[event_id]))


class MyEvents(generic.ListView):
    model = Event
    paginate_by = 16
    template_name = 'my_events.html'

    def get_queryset(self):
        events_owned = Event.objects.filter(
            approved=True,
            archived=False,
            owner=self.request.user
        )
        events_participating = Event.objects.filter(
            participants__id=self.request.user.id)
        return events_owned | events_participating


class LikeEvent(View):

    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        if request.user in event.likes.all():
            event.likes.remove(request.user)
        else:
            event.likes.add(request.user)
        next = request.POST.get('next', '/')
        return redirect(next)
