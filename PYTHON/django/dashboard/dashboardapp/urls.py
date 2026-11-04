from django.urls import path
from . import views

urlpatterns = [
    # Landing & Authentication
    path('', views.index),                      # Landing page (Welcome)
    path('signin/', views.signin_page),         # Render sign-in page
    path('login/', views.login_process),        # Process login POST
    path('register/', views.register_page),     # Render registration page
    path('register/process/', views.register_process), # Process registration POST
    path('logout/', views.logout),              # Clear session and log out

    # Dashboards (Admin vs Normal User)
    path('dashboard/', views.dashboard),        # Main dashboard view

    # Admin: Adding & Editing Users
    path('users/new/', views.new_user_page),    # Admin page to create a new user manually
    path('users/create/', views.create_user_process), # Process manual user creation POST
    path('users/edit/', views.edit_profile_page),     # Edit your own profile
    path('users/edit/<int:user_id>/', views.admin_edit_user_page), # Admin editing another user
    path('users/update/<int:user_id>/', views.update_user_process), # Process profile/password updates

    # User Profiles & Wall Messages
    path('users/show/<int:user_id>/', views.user_profile), # View specific user wall & profile details
    path('messages/create/<int:user_id>/', views.post_message), # Post a wall message on a user's profile
    path('users/destroy/<int:user_id>/', views.delete_user), # Admin removing a user
]