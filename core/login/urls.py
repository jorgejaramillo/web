from django.urls import path, re_path
from core.login.views import LoginView, LogoutView

urlpatterns = [
    re_path(r'^$', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
