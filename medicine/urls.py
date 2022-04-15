from django.contrib import admin
from django.urls import path
from . import views

app_name = 'medicine'

urlpatterns = [
    path('create/', views.index, name = 'index'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('addpatient/', views.addpatient, name = 'addpatient'),
    path('receteolustur/', views.receteolustur, name = 'receteolustur'),
    path('ilaclistesi/', views.ilacListesi, name = 'ilaclistesi'),
    path('recetelistesi/', views.receteListesi, name = 'recetelistesi'),
    path('medicine/<int:id>', views.deTail,name="detail"),
]