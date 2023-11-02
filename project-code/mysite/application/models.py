from django.db import models

# Use DOG API to create vars we want to save
class Dog(models.Model):
    name = models.CharField(max_length=50, blank = True, null = True)
    age = models.CharField(max_length=10, blank = True, null = True)
    weight = models.CharField(max_length=4000, blank = True, null = True)
    height = models.CharField(max_length=40, blank = True, null = True)
    traits = models.CharField(max_length=20, blank = True, null = True)
    image_url = models.ImageField( max_length=50, blank = True, null = True)

    def __str__(self):
        return self.name

class Dog_2(models.Model):
    name_2 = models.CharField(max_length=50, blank = True, null = True)
    age_2 = models.CharField(max_length=10, blank = True, null = True)
    weight_2 = models.CharField(max_length=4000, blank = True, null = True)
    height_2 = models.CharField(max_length=20, blank = True, null = True)
    traits_2 = models.CharField(max_length=20, blank = True, null = True)
    image_url_2 = models.ImageField( max_length=50, blank = True, null = True)

    def __str__(self):
        return self.name_2
    
