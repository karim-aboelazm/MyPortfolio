from django.contrib import admin
from .models import *

for i in [AboutMe, Skill, Service, Statistics, Portfolio,ProjectImages,Testimonial,Certifications,Jobs]:
    admin.site.register(i)