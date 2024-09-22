from django.urls import path
from .views import FollowView, UnfollowView
from . import views

urlpatterns = [
    path('register/', views.UserListView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('profile', ProfileView.as_view()),
    path('unfollow/<int:user_id>/', UnfollowView.as_view()),
]