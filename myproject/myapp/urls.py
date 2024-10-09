from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload-data/', views.upload_data, name='upload_data'),
    path('query-builder/', views.query_builder, name='query_builder'),
    path('users/', views.users, name='users'),
    path('upload/', views.upload_file, name='upload_file'),
]
