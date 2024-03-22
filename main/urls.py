from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('about/', views.about, name='about'),
    path('action/', views.action, name='action'),
    path('contact/', views.contact, name='contact'),
    path('doctores/', views.doctores, name='doctores'),
    path('news/', views.news_list, name='news_list'),
]
