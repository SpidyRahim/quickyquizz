from django.urls import path
from . import views

urlpatterns = [
    path('tsignup', views.teacher_signup_view, name='tsignup'),
    path('ssignup',views.student_signup_view, name='ssignup')
]