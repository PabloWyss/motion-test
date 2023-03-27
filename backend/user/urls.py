from django.urls import path

from user.views import ListUserView, UpdateFollowUsereView, ListFollowersView, ListFollowingView

urlpatterns = [
    path("", ListUserView.as_view()),
    path("followers/toggle-follow/<int:id>/", UpdateFollowUsereView.as_view()),
    path("followers/followers/", ListFollowersView.as_view()),
    path("followers/following/", ListFollowingView.as_view()),
]
