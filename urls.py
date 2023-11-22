from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
