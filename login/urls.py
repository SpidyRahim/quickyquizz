from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('tlogin', LoginView.as_view(template_name='tlogin.html'),name='tlogin'),
    path('slogin',LoginView.as_view(template_name='slogin.html'), name='slogin')
]