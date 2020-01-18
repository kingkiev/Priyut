from django.contrib import admin
from p_library.models import AnimalType, Pet, AnimalSex

@admin.register(AnimalType)
class AnimalTypeAdmin(admin.ModelAdmin):
	pass

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
	list_display = ('type_pet', 'name', 'pet_breed', 'sex', 'age')

@admin.register(AnimalSex)
class AnimalSexAdmin(admin.ModelAdmin):
	pass
	