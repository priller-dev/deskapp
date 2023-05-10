from django.urls import path
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from users.auth_views import (
    login_view, register_view
)

auth = [
    path('login', login_view, name='login_view'),
    path('register', register_view, name='register_view'),
    # path('forgot', forgot_view, name='forgot_view'),
    path('logout', LogoutView.as_view(next_page='index_view'), name='logout_view'),
    # path('password-reset/<str:user_id>/<str:token>', reset_view, name='reset_view'),
    path(
        'password-reset/',
        PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password-reset'
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'password-reset-complete/',
        PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'
    ),
]

users = []

urlpatterns = auth + users