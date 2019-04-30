from django.urls import path
from . import views

urlpatterns = [
     path('', views.main, name='main'),
     path('empty/<door_id>', views.empty, name='empty'),
     path('loaded/<door_id>', views.loaded, name='loaded'),
     path('in_progress/<door_id>', views.in_progress, name='in_progress'),
     path('clear/<door_id>', views.clear, name='clear'),
     path('edit/<door_id>', views.edit, name='edit'),
]
