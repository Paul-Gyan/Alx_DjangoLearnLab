from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('book/<int:pk>/', views.BookDetail.as_view()),
    path('books/create', views.BookCreateView.as_view()),
    path('books/<int:pk>/update', views.BookUpdateView.as_view()),
    path('books/<int:pk>/delete', views.BookDeleteView.as_view()),
    path('book/update/', views.BookUpdateView.as_view()),
    path('book/delete/', views.BookDeleteView.as_view()),

]




