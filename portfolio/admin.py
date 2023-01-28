from django.contrib import admin
from .models import *


for i in [AboutMe, Skill, Service, Statistics, 
          Portfolio,ProjectImages,Testimonial,
          Certifications,Jobs,Courses,Courses_Videos,
          Course_Lectures,Course_Benefits,Course_Requirements,
          Course_Reviews,Course_Homework,Students,
          Cart,CartCourse,CourseOrder]:
    admin.site.register(i)
