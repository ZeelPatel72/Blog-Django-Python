# from django.contrib import admin
from django.urls import path
from .views import ( 
    PostListView, 
PostDetailView, 
PostCreateView,
PostUpdateView,
PostDeleteView,
UserPostListView
)
from . import views

urlpatterns = [
    # navigated path comes here concates things in single qoutes here.
    path('',PostListView.as_view(),name = 'Blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name = 'post-detail'),
    path('post/new/',PostCreateView.as_view(),name = 'post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name = 'post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name = 'post-delete'),
    path('user/<str:username>',UserPostListView.as_view(),name = 'user-posts'),

    path('about/',views.about,name = 'Blog-about'),
]
