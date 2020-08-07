from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.PostListView.as_view(), name="post-list"),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name="post-detail"),
    path('post/category/<slug:category>/', views.PostCategoryView.as_view(), name="post-by-category"),
    path('post/tag/<slug:tag>/', views.TagListView.as_view(), name="post-by-tag"),
]