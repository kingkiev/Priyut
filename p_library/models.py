from django.db import models

class AnimalType(models.Model):
	animal_type = models.CharField(max_length=30)
	
	def __str__(self):
		return self.animal_type

class AnimalSex(models.Model):
	animal_sex = models.CharField(max_length=10)

	def __str__(self):
		return self.animal_sex

class Pet(models.Model):
	type_pet = models.ForeignKey(AnimalType, on_delete=models.CASCADE, related_name='type_pet')
	name = models.CharField(max_length=30)
	sex = models.ForeignKey(AnimalSex, on_delete=models.CASCADE, related_name='sex')
	pet_breed = models.CharField(max_length=50, blank=True)
	description = models.TextField(blank=True)
	age = models.SmallIntegerField()
	photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

	def __str__(self):
		return self.name

