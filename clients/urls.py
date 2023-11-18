"""Defines URL patterns for clients."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients', views.clients, name='clients'),
    path('clients/<int:client_id>/', views.client, name='client'),
    path('new_client/', views.new_topic, name='new_client'),
    path('edit_client/<int:client_id>', views.edit_client, name='edit_client')
]
