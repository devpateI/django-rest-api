from django.urls import path
from basic_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('articles/', views.article_list),
    path('articles/', views.ArticleAPIView.as_view()),
    # path('articles/<int:pk>/', views.article_detail),
    path('articles/<int:pk>/', views.ArticleDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)