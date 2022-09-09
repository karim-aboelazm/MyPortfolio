from django.contrib import admin
from .models import *

for i in [AboutMe, Skill, Service, Statistics, Portfolio,ProjectImages,Testimonial,Blog,Jobs]:
    admin.site.register(i)