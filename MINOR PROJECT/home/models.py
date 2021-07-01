from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to = 'photos/products')
    price = models.IntegerField()

class contact(models.Model):
    name = models.CharField(max_length=255)
    e_mail = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()

class subscribe(models.Model):
    email = models.EmailField()

class about_us(models.Model):
    description = models.TextField()
    about_image = models.ImageField(upload_to = 'photos/about')