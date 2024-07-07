from django.urls import path

from .views import HomePageView, ArticleListView, ArticleDetailView


urlpatterns = [
    path('', HomePageView.as_view(), name="homepage"),
    path('articles/', ArticleListView.as_view(), name="article_list"),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
]
