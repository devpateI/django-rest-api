from django.urls import path
from basic_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:pk>/', views.article_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)