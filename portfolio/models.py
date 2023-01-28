from django.db import models
from django.contrib.auth.models import User
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

class Courses(models.Model):
    title                = models.CharField(_('Course Title'), max_length=150)
    title_ar             = models.CharField(_('Course Title Arabic'), max_length=150)
    description_ar       = models.TextField(_('Course Description Arabic'))
    poster               = models.ImageField(upload_to='courses/posters/')
    language             = models.CharField(_('Course language'), max_length=150,blank=True)
    language_ar          = models.CharField(_('Course language Arabic'), max_length=150,blank=True)
    description          = models.TextField(_('Course Description'))
    started_at           = models.DateField(verbose_name=_('Started At'))
    ended_at             = models.DateField(verbose_name=_('Ended At'))
    price                = models.PositiveIntegerField(default=10,verbose_name=_('Course price'))
    discount             = models.PositiveIntegerField(default=0,verbose_name=_('Course Discount for Price'))
    price_after_discount = models.PositiveIntegerField(default=0,verbose_name=_('Course Price After Discount'),blank=True)
    def save(self, *args, **kwargs):
        self.price_after_discount = int(self.price - (self.price*self.discount)/100)
        super(Courses, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = _('Courses')
    
    def __str__(self):
        return self.title + " Course"

class Courses_Videos(models.Model):
    course               = models.ForeignKey(Courses,on_delete=models.CASCADE,verbose_name=_('course'))
    title                = models.CharField(_('Course Video Title'), max_length=150)
    title_ar             = models.CharField(_('Course Video Title Arabic'), max_length=150)
    description          = models.TextField(_('Course Video Description'),max_length=100)
    description_ar       = models.TextField(_('Course Video Description Arabic'),max_length=100)
    poster               = models.ImageField(upload_to='courses/Videos/Posters/',verbose_name=_('poster'))
    video                = models.FileField(upload_to='courses/Videos/',verbose_name=_('Video'))
    video_duration_in_min= models.PositiveSmallIntegerField(default=0,verbose_name=_('Video Duration in Minutes ?'))
    video_number         = models.PositiveSmallIntegerField(default=0,verbose_name=_('Video Number ?'))
    
    class Meta:
        verbose_name_plural = _('Courses Videos')
    
    def __str__(self):
        return f"Video : {self.title} - number : {self.video_number} - for course : {self.course.title}"

class Course_Lectures(models.Model):
    course               = models.ForeignKey(Courses,on_delete=models.CASCADE,verbose_name=_('course'))
    title                = models.CharField(_('Course Lectures Title'), max_length=150)
    title_ar             = models.CharField(_('Course Lectures Title Arabic'), max_length=150)
    description          = models.TextField(_('Course Lectures Description'))
    description_ar       = models.TextField(_('Course Lectures Description Arabic'))
    content_in_pdf       = models.FileField(upload_to='courses/content_pdfs/',verbose_name=_('content in pdf'))
    Content_number       = models.PositiveSmallIntegerField(default=0,verbose_name=_('Content number ?'))
    class Meta:
        verbose_name_plural = _('Courses Lectures')
    
    def __str__(self):
        return f"{self.title} - number : {self.Content_number} - for course : {self.course.title}"

class Course_Benefits(models.Model):
    course               = models.ForeignKey(Courses,on_delete=models.CASCADE,verbose_name=_('course'))
    benefit              = models.CharField(_('Course Benefit item'), max_length=150)
    
    class Meta:
        verbose_name_plural = _('Courses Benefits')
    
    def __str__(self):
        return f"{self.benefit} - for course : {self.course.title}"
    
class Course_Requirements(models.Model):
        course               = models.ForeignKey(Courses,on_delete=models.CASCADE,verbose_name=_('course'))
        requirement          = models.CharField(_('Course Benefit item'), max_length=150)
    
        class Meta:
            verbose_name_plural = _('Course Requirements')
        
        def __str__(self):
            return f"{self.requirement} - for course : {self.course.title}"

class Course_Reviews(models.Model):
    RATING_CHOICES = ((i,str(i)) for i in range(1,6))
    course   = models.ForeignKey(Courses,on_delete=models.CASCADE,verbose_name=_('course'))
    pub_date = models.DateTimeField(_('date published'),auto_now_add=True)
    user_name = models.CharField(_('User'), max_length=100)
    comment = models.TextField(_('Comment'))
    rating = models.IntegerField(_('Rating'),choices=RATING_CHOICES,default=1)
    
    class Meta:
        verbose_name_plural = _('Course Reviews')
        
    def __str__(self):
        return f"The Rate of {self.course.title} is {self.rating}/5.  by {self.user_name}"

class Course_Homework(models.Model):
    course      = models.ForeignKey(Courses,on_delete=models.CASCADE,verbose_name=_('course'))
    task        = models.CharField(_('task'), max_length=300)
    task_number = models.PositiveSmallIntegerField(default=0,verbose_name=_('task number ?'))
    class Meta:
        verbose_name_plural = _('Course Homework')
        
    def __str__(self):
        return f"Task Number : {self.task_number} for {self.course.title} Course"

class Students(models.Model):
    user = models.OneToOneField(User,verbose_name=_("username"), on_delete=models.CASCADE)
    full_name = models.CharField(_("full_name"),max_length=200)
    address = models.CharField(_("address"),max_length=200, null=True, blank=True)
    image = models.ImageField(_("image"),upload_to='students/')
    phone = models.CharField(_("phone"),max_length=15,blank=True, null=True)
    join_on = models.DateTimeField(_("join_on"),auto_now_add=True)
    class Meta:
        verbose_name_plural = _("Students")
        
    def __str__(self):
        return self.full_name

# cart database fields
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete = models.SET_NULL, blank = True, null=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return "Cart : " + str(self.id)

# cart product database fields
class CartCourse(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    course = models.ForeignKey(Courses , on_delete = models.CASCADE)
    rate = models.PositiveIntegerField()            
    subtotal = models.PositiveIntegerField() 
    def __str__ (self):
        return "Cart : " + str(self.cart.id) +" CartCourse : "+ str(self.id)

# order database fields
class CourseOrder(models.Model):
    cart = models.OneToOneField(Cart,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete = models.SET_NULL, blank = True, null=True)
    first_name = models.CharField(max_length=200,null=True) 
    last_name = models.CharField(max_length=200,null=True) 
    phone_num = models.CharField(max_length=15)
    email = models.EmailField(null=True , blank = True)
    subtotal = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    payment_mode = models.CharField(max_length=200,null=True)  
    payment_id = models.CharField(max_length=200,null=True) 
    def __str__(self):
        return "Order : "+ str(self.id)

    