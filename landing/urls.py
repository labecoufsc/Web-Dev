from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('boias/', views.boias, name='boias'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('mapaFlorianopolis/', views.mapaFlorianopolis, name='mapaFlorianopolis'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)