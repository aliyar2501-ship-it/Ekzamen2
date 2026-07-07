from django.urls import path
from . import views

urlpatterns = [
    path('', views.ad_list, name='ad_list'),
    path('ad/<int:pk>/', views.ad_detail, name='ad_detail'),
    path('ad/new/', views.ad_create, name='ad_create'),
    path('ad/<int:pk>/edit/', views.ad_update, name='ad_update'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('register/', views.register, name='register'),
]