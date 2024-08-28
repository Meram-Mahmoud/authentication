# users/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, CustomPasswordChangeView
from django.contrib.auth.views import LogoutView
from .views import CustomPasswordResetView



urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', ), name='login'),
 path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html'  
    ), name='password_reset'),    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('password-change/', CustomPasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
        path('custom-password-reset/', CustomPasswordResetView.as_view(), name='custom_password_reset'),

]
