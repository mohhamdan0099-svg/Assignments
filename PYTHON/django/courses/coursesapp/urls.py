from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('courses/create', views.create_course),
    path('courses/destroy/<int:id>', views.destroy_page),
    path('courses/remove/<int:id>', views.destroy),
]