from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create_idea, name='create_idea'),
  path('idea/<int:pk>/', views.get_idea, name='detail_idea'),
]