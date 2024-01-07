from django.urls import path
from . import views
from .views import EditProfile
urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/<int:pk>/', views.EditProfile.as_view(), name='edit_profile'),
]