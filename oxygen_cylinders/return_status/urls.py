from django.urls import path, re_path, include

from .views import SourcesController

urlpatterns = [
    path('sources/save', SourcesController.as_view({'post': 'saving_data'})),
    path('getdata', SourcesController.as_view({'get': 'retrive_data'}))
    ]