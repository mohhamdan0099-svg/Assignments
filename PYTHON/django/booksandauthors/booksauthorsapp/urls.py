from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),                             
    path('books/create', views.add_book),
    path('books/<int:book_id>', views.view_book),
    path('books/<int:book_id>/add_author', views.add_author_to_book),
    
    path('authors', views.authors_page),
    path('authors/create', views.add_author),
    path('authors/<int:author_id>', views.view_author),
    path('authors/<int:author_id>/add_book', views.add_book_to_author),
    path('new_page/',views.new_page),
    path('submit',views.submit)
]