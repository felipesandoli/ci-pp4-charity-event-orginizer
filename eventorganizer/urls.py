from . import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout', views.Logout.as_view(), name='logout_view'),
    path('create-event', views.CreateEvent.as_view(), name='create_event'),
    path(
        'event/<pk>',
        views.EventInformation.as_view(),
        name='event_information'
    ),
    path('event/<int:event_id>/edit', views.EditEvent.as_view(), name='edit_event')
]
