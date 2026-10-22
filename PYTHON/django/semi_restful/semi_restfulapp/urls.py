from django.urls import path
from . import views

urlpatterns=[
    path('',views.start),
    path('shows/',views.all_shows),
    path('shows/new/',views.index),
    path('create/',views.create),
    path('shows/delete/<int:id>',views.delete),
    path('shows/<int:id>/',views.new_show),
    path('shows/edit/<int:id>',views.edit),
    path('shows/edit/<int:id>/update/',views.update),
    
]