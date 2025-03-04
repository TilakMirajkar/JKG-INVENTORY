from django.urls import path
from .views import CustomLoginView, RegistrationView, custom_logout_view

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', custom_logout_view, name='logout'),
]