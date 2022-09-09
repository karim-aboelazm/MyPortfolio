from django.urls import path
from .views import *

app_name = 'portfolio'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('project-<pk>-detail/', ProjectDetailView.as_view(), name='project-details'),
]