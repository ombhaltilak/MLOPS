# filepath: /c:/Users/om/Desktop/aissmsioit/webapp/webapp/urls.py
from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
]