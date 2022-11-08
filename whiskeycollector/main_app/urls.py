from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('whiskey/', views.whiskey_index, name='index'),
    path('whiskey/<int:whiskey_id>/', views.whiskey_detail, name='detail'),
]