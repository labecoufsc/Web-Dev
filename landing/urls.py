from django.urls import path
from . import views

urlpatterns = [
    path('boias/', views.boias, name='boias'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('mapaFlorianopolis', views.mapaFlorianopolis, name='mapaFlorianopolis'),
]