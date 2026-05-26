from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mission/', views.mission, name='mission'),
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),
    path('payment/', views.payment_portal, name='payment'),
    path('gallery/', views.gallery, name='gallery'),
    path('announcements/', views.announcements, name='announcements'),
    path('calendar/', views.school_calendar, name='school_calendar'),
]
