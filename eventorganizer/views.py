from django.shortcuts import render
from django.views import View


class HomePage(View):
    template_name = 'index.html'
