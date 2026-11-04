from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_dashboard),
    path('add_book/', views.add_book),
    path('<int:book_id>/', views.book_detail),
    path('<int:book_id>/update/', views.update_book),
    path('<int:book_id>/delete/', views.delete_book),
    path('<int:book_id>/favorite/', views.toggle_favorite),
]