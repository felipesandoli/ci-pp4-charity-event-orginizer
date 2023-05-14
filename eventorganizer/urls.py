from . import views
from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomePage.as_view(), name="homepage"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("logout", views.Logout.as_view(), name="logout_view"),
    path("create-event", views.CreateEvent.as_view(), name="create_event"),
    path(
        "event/<int:event_id>",
        views.EventInformation.as_view(),
        name="event_information",
    ),
    path("event/<int:event_id>/edit", views.EditEvent.as_view(), name="edit_event"),
    path(
        "event/<int:event_id>/delete", views.DeleteEvent.as_view(), name="delete_event"
    ),
    path("event/<int:event_id>/join", views.JoinEvent.as_view(), name="join_event"),
    path("event/<int:event_id>/leave", views.LeaveEvent.as_view(), name="leave_event"),
    path("my-events", views.MyEvents.as_view(), name="my_events"),
    path("event/<int:event_id>/like", views.LikeEvent.as_view(), name="like_event"),
]
