from django.views.generic import TemplateView,FormView,CreateView,UpdateView
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.views import PasswordChangeView
from .utils import password_reset_token
from django.http import JsonResponse
from django.views.generic.base import View
from django.shortcuts import render, get_object_or_404,redirect
from django.shortcuts import render,reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse_lazy
from django.conf import settings
from .models import *
from .forms import *



class PortofolioMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Students.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/student-login/")
        return super().dispatch(request, *args, **kwargs)

class HomePageView(FormView):
    template_name = 'home_pages/home.html' 
    form_class = ContactForm
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutMe.objects.latest('id')
        context['jobs'] = Jobs.objects.all().order_by('-id')
        context['skills'] = Skill.objects.all().order_by('-id')
        context['services'] = Service.objects.all().order_by('-id')
        context['statistics'] = Statistics.objects.all()
        context['portfolio'] = Portfolio.objects.all().order_by('-id')
        context['testimonials'] = Testimonial.objects.all()
        context['Certifications'] = Certifications.objects.all().order_by('-id')
        return context
    
    def form_valid(self, form):
        Name = form.cleaned_data.get('name')
        Email = form.cleaned_data.get('email')
        Subject = form.cleaned_data.get('subject')
        Message = form.cleaned_data['message']
        msg = f"""
        Hello Sir,

        I am {Name} and my email is {Email} .

        All Details is {Message}.

        Thank You!
        """
        send_mail(
            Subject,
            msg,
            Email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return super().form_valid(form)
    
class ProjectDetailView(TemplateView):
    template_name = 'project_pages/project-details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutMe.objects.latest('id')
        context['jobs'] = Jobs.objects.all().order_by('-id')
        context['portfolio'] = Portfolio.objects.get(id = self.kwargs['pk'])
        return context

class AllCoursesView(TemplateView):
    template_name = 'course_pages/courses.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutMe.objects.latest('id')
        context['jobs'] = Jobs.objects.all().order_by('-id')
        context["course_list"] = Courses.objects.all().order_by('-id') 
        return context

class CourseDetailView(PortofolioMixin,TemplateView):
    template_name = 'course_pages/one_course.html'
    def get_context_data(self ,**kwargs):
        context = super().get_context_data(**kwargs)
        course = Courses.objects.get(id=self.kwargs['pk'])
        context["course_payment_value"] = course.price_after_discount * 100
        context["course"] = course
        
        context["order"] = []
        context["paid_courses"] = []
        
        for i in self.request.user.courseorder_set.all():
            context["order"].append(i)
        for j in context["order"]:
            order_course  = CartCourse.objects.get(cart=j.cart).course
            context["paid_courses"].append(Courses.objects.get(id=order_course.id).title)
        
        if course.title in context["paid_courses"]:
            context["course_had_paid"] = "done"
        else:
            context["course_had_paid"] = "not done"
            
        return context
    
# customer registeration
class StudentRegisterView(CreateView):
    template_name = 'student_pages/signup.html'
    form_class = StudentRegisterForm
    success_url = reverse_lazy('porto:home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        full_name = form.cleaned_data.get('full_name')
        user = User.objects.create_user(username=username,email=email,password=password,first_name=full_name.split(" ")[0],last_name=full_name.split(" ")[-1])
        form.instance.user = user
        login(self.request , user)
        return super().form_valid(form)

# customer logout
class StudentLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('porto:home')

# customer logout
class StudentLoginView(FormView):
    template_name = 'student_pages/login.html'
    form_class = StudentLoginForm
    success_url = reverse_lazy('porto:home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self,form):
        user_name = form.cleaned_data.get('username')
        pass_word = form.cleaned_data['password']
        usr = authenticate(username=user_name,password=pass_word)
        if usr is not None and Students.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request,self.template_name,{'form':self.form_class})
        return super().form_valid(form)
    
    def get_success_url(self):
        if 'next' in self.request.GET:
            next_url = self.request.GET.get('next')
            return next_url
        else:
            return self.success_url

# customer profile
class StudentProfileView(PortofolioMixin,TemplateView):
    template_name = "student_pages/profile.html"
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.students:
            pass
        else:
            return redirect("/student-login/?next=/student-profile/")
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order"] = []
        context["student_courses"] = []
        
        for i in self.request.user.courseorder_set.all():
            context["order"].append(i)
        for j in context["order"]:
            order_course  = CartCourse.objects.get(cart=j.cart).course
            context["student_courses"].append(Courses.objects.get(id=order_course.id))
        
        context["profile"] = Students.objects.get(user=self.request.user) 
        context['about'] = AboutMe.objects.latest('id')
        context['jobs'] = Jobs.objects.all().order_by('-id')
        context["student_courses"] = list(set(context["student_courses"]))[::-1]
        return context

# customer update profile
class UpdateProfileView(PortofolioMixin,UpdateView):
    model = Students
    form_class = ProfileUpdateForm
    template_name = 'student_pages/edit_profile.html'
    
    def get_object(self, *args, **kwargs):
        customer = get_object_or_404(Students, pk=self.kwargs['pk'])
        return customer
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutMe.objects.latest('id')
        context['jobs'] = Jobs.objects.all().order_by('-id')
        return context
    
    def get_success_url(self, *args, **kwargs):
        success_url = reverse_lazy('porto:student_profile')
        return success_url

class ForgotPasswordView(FormView):
    template_name = 'student_pages/forgot_password.html'
    form_class = PasswordForm
    success_url = "/forgot-password/?m=s"
    def form_valid(self,form):
        # get email from user
        email = form.cleaned_data.get("email")
        # get current host ip/Domain [127.0.0.1:8000]
        url = self.request.META['HTTP_HOST']
        # get customer and then user
        customer = Students.objects.get(user__email = email)
        user = customer.user
        # sent mail to customer with email
        text_content = 'Please click the link below to reset your password.  '
        html_content = url + "/reset-password/" + email +"/" + password_reset_token.make_token(user)+"/"
        send_mail(
            'Password Reset Link | Karim Mohammed Aboelazm',
            text_content + html_content,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently = False,
            
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ResetPasswordView(FormView):
    template_name = 'student_pages/reset_password.html'
    form_class = PasswordResetForm
    success_url = '/student-login/'
    
    def dispatch(self, request, *args, **kwargs):
        email = self.kwargs.get("email")
        user = User.objects.get(email=email)
        token = self.kwargs.get("token")
        if user is not None and password_reset_token.check_token(user,token):
           pass
        else:
            return redirect(reverse('porto:forgot_password')+'?m=e')
        return super().dispatch(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        return context
    
    def form_valid(self,form):
        password = form.cleaned_data['new_password']
        email = self.kwargs.get("email")
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
        return super().form_valid(form)

class ChangePasswordView(PasswordChangeView):
    template_name = 'student_pages/change_password.html'
    success_url = '/'
    
# add product to my cart
class AddToCartView(TemplateView):
    template_name = "cart_pages/add_to_cart.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_obj = Courses.objects.get(id=self.kwargs['pk'])
        context["order"] = []
        context["student_courses"] = []
        
        for i in self.request.user.courseorder_set.all():
            context["order"].append(i)
        for j in context["order"]:
            order_course  = CartCourse.objects.get(cart=j.cart).course
            context["student_courses"].append(Courses.objects.get(id=order_course.id))
        if course_obj in context["student_courses"]:
            context["course_exist"] = True
        else:
            context["course_exist"] = False
        context["course"] = course_obj
        cart_id = self.request.session.get('cart_id',None)
        
        if cart_id:
            cart = Cart.objects.get(id = cart_id)
            this_course_in_cart = cart.cartcourse_set.filter(course=course_obj)
            if this_course_in_cart.exists():
                cartcourse = this_course_in_cart.last()
                # cartcourse.quantity += 1
                cartcourse.subtotal += course_obj.price_after_discount
                cartcourse.save()
                cart.total += course_obj.price_after_discount
                cart.save()
            else:
                cartcourse = CartCourse.objects.create(cart=cart,course=course_obj,rate=course_obj.price_after_discount,subtotal=course_obj.price_after_discount)
                cart.total += course_obj.price_after_discount
                cart.save()
        else:
            cart = Cart.objects.create(user=self.request.user,total=0)
            self.request.session['cart_id'] = cart.id
            cartcourse = CartCourse.objects.create(cart=cart,course=course_obj,rate=course_obj.price_after_discount,subtotal=course_obj.price_after_discount)
            cart.total += course_obj.price_after_discount
            cart.save()
        return context

# my cart page view
class CartView(TemplateView):
    template_name = "cart_pages/cart.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id',None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context["cart"] = cart 
        
        return context

# manage in items that are in cart 
class ManageCartView(View):
    def get(self,request,*args, **kwargs):
        action = request.GET.get('action')
        cp_obj = CartCourse.objects.get(id = self.kwargs['pk'])
        cart_obj = cp_obj.cart  
        if action == 'rcr':
            cart_obj.total -= cp_obj.subtotal
            cart_obj.save()
            cp_obj.delete()
        else:
            pass
        return redirect('/my-cart/')

# empty the cart form orders 
class EmptyCartView(PortofolioMixin,View):
    def get(self, request, *args, **kwargs):
        cart_id = request.session.get('cart_id',None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
            cart.cartcourse_set.all().delete()
            cart.total = 0
            cart.save()
        return redirect('/my-cart/')

# check out page view
class CheckOutView(PortofolioMixin, FormView):
    template_name = "cart_pages/check_out.html"
    form_class = CheckOutForm
    success_url = reverse_lazy('porto:home')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.students:
            pass
        else:
            return redirect("/student-login/?next=/check-out/")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Students.objects.get(user=self.request.user)
        context["client_id"] = settings.PAYPAL_CLIENT_ID
        cart_id = self.request.session.get('cart_id',None)
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
        else:
            cart_obj = None
        context["cart"] = cart_obj
        return context
    
    def form_valid(self,form):
        cart_id = self.request.session.get('cart_id')
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            form.instance.user = self.request.user
            form.instance.cart = cart_obj
            form.instance.subtotal = cart_obj.total
            form.instance.total = cart_obj.total
            form.instance.payment_mode = "Paid by PayPal"
            form.instance.payment_id   = self.request.POST.get("payment_id") 
            del self.request.session['cart_id']
            order = form.save()
            return redirect('/')
        else:
            return redirect('porto:home')
        return super().form_valid(form)
  
class CheckOutWithRazorPay(PortofolioMixin,View):
    def get(self, request,*args, **kwargs):
        cart_id = self.request.session.get('cart_id',None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
            total_price = cart.total
            # for item in cart.cartcourse_set.all:
            #     total_price += item.total
            return JsonResponse({
                "total_price":total_price
                })
        else:
            cart = None
            total_price = 0
            return JsonResponse({
                "total_price":total_price
                })
                
class PaypalRequestView(PortofolioMixin,View): 
    def get(self, request,*args, **kwargs):
        context={"order" : CourseOrder.objects.get(id = request.GET.get("o_id")),"client_id" : settings.PAYPAL_CLIENT_ID}
        return render(request,'payment_pages/paypalrequest.html',context)

class CreditCardRequestView(PortofolioMixin,View):
    def get(self, request,*args, **kwargs):
        context={"order":CourseOrder.objects.get(id = request.GET.get("o_id"))}
        return render(request,'payment_pages/credit_card_request.html',context)

class OrderHadFinishedView(PortofolioMixin,FormView):
    template_name= "order_pages/order_content.html"
    form_class = ReviewForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["course"] = Courses.objects.get(id=self.kwargs['pk'])
        return context
    
    def get_course(self, **kwargs):
        course = Courses.objects.get(id=self.kwargs['pk'])
        return course
    
    def form_valid(self, form):
        form.instance.course = self.get_course()
        form.instance.save()
        return super(OrderHadFinishedView,self).form_valid(form)
    
    def get_success_url(self):
           return reverse_lazy('porto:order_had_finished', kwargs={'usr': self.kwargs['usr']})
    
    

