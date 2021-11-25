from django.urls import path
from basic_api import views

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:pk>/', views.article_detail),
]