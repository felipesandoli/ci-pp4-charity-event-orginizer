from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('signup/', views.SignUp.as_view(), name='signup')
]
