from django.urls import path
from . import views

urlpatterns = [
    # other URL patterns
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]