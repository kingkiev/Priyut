from django import forms
from p_library.models import Pet

class PetForms(forms.ModelForm):
	class Meta:
		model = Pet
		fields = '__all__'