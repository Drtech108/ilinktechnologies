
from django.urls import include, path

from myapp import views

urlpatterns = [
   path('', views.home, name='home'),
   path('services/', views.services, name='services'),
   path('gallery/', views.gallery, name='gallery'),
   path('contact/', views.contact_view, name='contact'),
   path('about/', views.about, name='about'),
   path('registration/', views.registration_view, name='registration'),
   path('registration/success/', views.registration_success, name='registration_success'),
]
