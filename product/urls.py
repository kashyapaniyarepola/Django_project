from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='product-home'),
    path('add/', views.add , name='product-add'),
]
