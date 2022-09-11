from django.db import models
from django.utils.translation import gettext_lazy as _

class AboutMe(models.Model):
    name          = models.CharField(max_length=150, verbose_name=_('name'))
    name_ar       = models.CharField(max_length=150, verbose_name=_('name_ar'))
    description   = models.TextField(verbose_name=_('description'))
    description_ar= models.TextField(verbose_name=_('description_ar'))
    image         = models.ImageField(upload_to='images/', verbose_name=_('image'))
    job           = models.CharField(max_length=150, verbose_name=_('job'))
    job_ar        = models.CharField(max_length=150, verbose_name=_('job_ar'))
    email         = models.EmailField(verbose_name=_('email'))
    phone         = models.CharField(max_length=15, verbose_name=_('phone'))
    address       = models.CharField(max_length=150, verbose_name=_('address'))
    address_ar    = models.CharField(max_length=150, verbose_name=_('address_ar'))
    facebook      = models.URLField(verbose_name=_('facebook'))       
    github        = models.URLField(verbose_name=_('github'))
    whatsapp      = models.CharField(max_length=15,verbose_name=_('whatsapp'))
    linkedin      = models.URLField(verbose_name=_('linkedin'))
    Resume        = models.FileField(upload_to='resumes/', verbose_name=_('Resume'))
    class Meta:
        verbose_name_plural = _('About Me')
    def __str__(self):
        return self.name

class Jobs(models.Model):
    jobs_for       = models.ForeignKey(AboutMe, on_delete=models.CASCADE, verbose_name=_('jobs_for'))
    title          = models.CharField(max_length=150, verbose_name=_('title'))
    title_ar       = models.CharField(max_length=150, verbose_name=_('title_ar'))
    class Meta:
        verbose_name_plural = _('Jobs')
    def __str__(self):
        return self.title

class Skill(models.Model):
    title         = models.CharField(max_length=50, verbose_name=_('title'))
    rate          = models.IntegerField(verbose_name=_('rate'),default=0)
    class Meta:
        verbose_name_plural = _('Skills')
    def __str__(self):
        return self.title

class Service(models.Model):
    title         = models.CharField(max_length=50, verbose_name=_('title'))
    title_ar      = models.CharField(max_length=50, verbose_name=_('title_ar'))
    description   = models.TextField(verbose_name=_('description'))
    description_ar= models.TextField(verbose_name=_('description_ar'))
    icon          = models.CharField(max_length=50, verbose_name=_('icon'))
    class Meta:
        verbose_name_plural = _('Service')
    def __str__(self):
        return self.title

class Statistics(models.Model):
    title         = models.CharField(max_length=50, verbose_name=_('title'))
    title_ar      = models.CharField(max_length=50, verbose_name=_('title_ar'))
    number        = models.IntegerField(verbose_name=_('number'))
    icon          = models.CharField(max_length=50, verbose_name=_('icon'))
    class Meta:
        verbose_name_plural = _('Statistics')
    def __str__(self):
        return self.title

class Portfolio(models.Model):
    project_name   = models.CharField(max_length=100, verbose_name=_('project_name'))
    project_name_ar= models.CharField(max_length=100, verbose_name=_('project_name_ar'))
    category       = models.CharField(max_length=50, verbose_name=_('category'))
    category_ar    = models.CharField(max_length=50, verbose_name=_('category_ar'))
    client         = models.CharField(max_length=50, verbose_name=_('client'))
    client_ar      = models.CharField(max_length=50, verbose_name=_('client_ar'))
    project_date   = models.DateField(verbose_name=_('project_date'))
    project_url    = models.URLField(verbose_name=_('project_url'))
    project_image  = models.ImageField(upload_to='images/', verbose_name=_('project_image'))
    project_desc   = models.TextField(verbose_name=_('project_desc'))
    project_desc_ar= models.TextField(verbose_name=_('project_desc_ar'))
    class Meta:
        verbose_name_plural = _('Portfolio')
    def __str__(self):
        return self.project_name

class ProjectImages(models.Model):
    project       = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    image         = models.ImageField(upload_to='project_images/', verbose_name=_('image'))
    class Meta:
        verbose_name_plural = _('ProjectImages')
    def __str__(self):
        return f"{self.project.project_name}"

class Testimonial(models.Model):
    name          = models.CharField(max_length=50, verbose_name=_('name'))
    name_ar       = models.CharField(max_length=50, verbose_name=_('name_ar'))
    job           = models.CharField(max_length=50, verbose_name=_('job'))
    job_ar        = models.CharField(max_length=50, verbose_name=_('job_ar'))
    image         = models.ImageField(upload_to='images/', verbose_name=_('image'))
    description   = models.TextField(verbose_name=_('description'))
    description_ar= models.TextField(verbose_name=_('description_ar'))
    class Meta:
        verbose_name_plural = _('Testimonial')
    def __str__(self):
        return self.name

class Certifications(models.Model):
    image         = models.ImageField(upload_to='images/', verbose_name=_('image'))
    class Meta:
        verbose_name_plural = _('Certifications')
    def __str__(self):
        return f"certification number : {self.id}"

