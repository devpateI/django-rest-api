from django.urls import path, include
from basic_api import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles',views.ArticleViewset,basename='articles')

urlpatterns = [
    # path('articles/', views.article_list),
    # path('articles/<int:pk>/', views.article_detail),
    path('articles/', views.ArticleAPIView.as_view()),
    path('articles/<int:pk>/', views.ArticleDetail.as_view()),
    path('generic/articles/' ,views.GenericArticleAPIView.as_view()),
    path('generic/articles/<int:id>/' ,views.GenericDetailApiView.as_view()),
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>',include(router.urls)),
]
# urlpatterns = format_suffix_patterns(urlpatterns)