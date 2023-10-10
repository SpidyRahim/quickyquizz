from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('qna',views.qa, name='qna'),
    path('review/<int:pk>',views.review, name='review'),
    path('dashboard', views.dashboard, name='teacher-dashboard'),
    path('delete-quiz/<int:pk>', views.delete_exam_view, name='delete'),
    path('logout', views.logout_view, name='logout')
]