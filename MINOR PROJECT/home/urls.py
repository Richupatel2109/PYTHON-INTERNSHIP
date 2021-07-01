from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.aboutus, name="about"),
    path('contact', views.contactus, name="contact"),
    path('furnitures', views.furnitures, name="furnitures"),
    path('blog', views.blog, name="blog"),
]