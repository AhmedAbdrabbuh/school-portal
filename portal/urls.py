from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mission/', views.mission, name='mission'),
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),
    path('payment/', views.payment_portal, name='payment'),
]
