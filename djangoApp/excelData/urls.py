from django.urls import path, include
from . import views

urlpatterns = [
    path('excelData/', views.excelData, name='excel_Data'),
]
