from django.shortcuts import render
from p_library.models import Pet
from p_library.forms import PetForms
from django.views.generic import ListView, TemplateView
from django.template import loader
from django.http import HttpResponse

class PetList(ListView):
	model = Pet
	template_name = 'pet_list.html'

class Index(TemplateView):
	template_name = "index.html"
