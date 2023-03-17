from django.contrib import admin
from django.urls import path

from post.views import ListCreatePostView, RetrieveUpdateDeletePostView, UpdateLikedPostView, ListLikedPostView

urlpatterns = [
    path("", ListCreatePostView.as_view()),
    path("<int:id>/", RetrieveUpdateDeletePostView.as_view()),
    path("likes/", ListLikedPostView.as_view()),
    path("toggle-like/<int:id>/", UpdateLikedPostView.as_view()),
]
