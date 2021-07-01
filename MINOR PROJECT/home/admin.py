from django.contrib import admin
from .models import product, about_us, contact, subscribe

# Register your models here.
admin.site.register(product)
admin.site.register(about_us)
admin.site.register(contact)
admin.site.register(subscribe)