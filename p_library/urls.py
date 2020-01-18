from django.contrib import admin
from django.urls import path
from .views import PetList

app_name = 'p_library'
urlpatterns = [
	path('pet_list', PetList.as_view(), name='pet_list'),
	# path('', index, name='index'),
	]