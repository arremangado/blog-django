from django.urls import path
from . import views
from .views import PostDeleteView
from .views import register

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:id>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('register/', register, name='register'),
]
