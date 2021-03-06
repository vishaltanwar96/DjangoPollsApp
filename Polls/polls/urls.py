from django.urls import include, path
from . import views

urlpatterns: list = [
    path('', views.index, name='index'),
    path('detail/<int:question_id>/', views.detail, name='question_detail'),
    path('result/<int:question_id>/', views.result, name='question_result'),
    path('vote/<int:question_id>/', views.index, name='vote')
]
