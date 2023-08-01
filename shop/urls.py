from django.urls import path
from . import views

urlpatterns = [
    # other URL patterns
    path('', views.home, name='home'),
]