from django import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from books.api import viewsets
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', viewsets.BooksList, name="books"),
    path('create/', viewsets.BookCreate, name="create"),
    path('detail/<str:pk>/', viewsets.BookDetail, name="detail"),
    path('update/<str:pk>/', viewsets.BookUpdate, name="update"),
    path('delete/<str:pk>/', viewsets.BookDelete, name="delete"),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
