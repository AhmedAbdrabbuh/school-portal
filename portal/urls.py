from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('payment/', views.payment_portal, name='payment'),
]
