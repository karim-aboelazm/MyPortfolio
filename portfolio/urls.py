from django.urls import path
from .views import *

app_name = 'portfolio'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('project-<pk>-detail/', ProjectDetailView.as_view(), name='project-details'),
    # path('courses/',AllCoursesView.as_view(),name="courses"),
    # path('course-<pk>-detail/',CourseDetailView.as_view(),name="course-details"),
]