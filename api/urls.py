from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.user_list, name='user-list'),
    path('api/categories/', views.category_list, name='category-list'),
    path('api/authors/', views.author_list, name='author-list'),
    path('api/books/', views.books_list, name='book-list'),
    path('api/books/<int:pk>/reviews/', views.review_list, name='review-list'),
    path('api/quotes/', views.quotes_list, name='quotes-list'),
]
