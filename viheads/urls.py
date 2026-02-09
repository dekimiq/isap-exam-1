from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create_idea, name='create_idea'),
  path('idea/<int:pk>/', views.get_idea, name='detail_idea'),
  path('idea/<int:pk>/edit/', views.update_idea, name='update_idea'),
  path('idea/<int:pk>/delete/', views.delete_idea, name='delete_idea'),
]