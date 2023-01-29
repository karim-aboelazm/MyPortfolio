from django.urls import path
from .views import *

app_name = 'portfolio'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('project-<pk>-detail/', ProjectDetailView.as_view(), name='project-details'),
    path('courses/',AllCoursesView.as_view(),name="courses"),
    path('course-<pk>-detail/',CourseDetailView.as_view(),name="course-details"),
    path('student-register/',StudentRegisterView.as_view(),name='student_register'),
    path('student-login/',StudentLoginView.as_view(),name='student_login'),
    path('student-logout/',StudentLogoutView.as_view(),name='student_logout'),
    path('student-profile/',StudentProfileView.as_view(),name='student_profile'),
    path('student-edit-profile/<int:pk>/',UpdateProfileView.as_view(),name='student_edit_profile'),
    path('forgot-password/',ForgotPasswordView.as_view(),name="forgot_password"),
    path('change-password/<int:pk>/',ChangePasswordView.as_view(),name="change_password"),
    path('reset-password/<email>/<token>/',ResetPasswordView.as_view(),name="reset_password"),
    # cart url
    path('my-cart/',CartView.as_view(),name='my_cart'),
    path('add-to-cart/<int:pk>/',AddToCartView.as_view(),name='add_to_cart'),
    path('manage-cart/<int:pk>/',ManageCartView.as_view(),name='manage_cart'),
    path('empty-cart/',EmptyCartView.as_view(),name='empty_cart'),
     # check out url
    path('check-out/',CheckOutView.as_view(),name='check_out'),
    path('proceed-to-pay/',CheckOutWithRazorPay.as_view(),name='proceed_to_pay'),
    # payments methods with khalti url
    path("paypal-request/", PaypalRequestView.as_view(), name="paypal_request"),
    
    # payments methods with esewa url
    path('credit-card-request/',CreditCardRequestView.as_view(), name="credit_card_request"),
    path('course-<int:pk>-had-payment-by-username-<str:usr>-paidwithpaypalAndPaymentStatusIsCompleted/',OrderHadFinishedView.as_view(),name="order_had_finished"),
    
    
]
   