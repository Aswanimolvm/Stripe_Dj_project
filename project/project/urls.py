from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
   
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_view, name='register'),
    path('',views.index,name='index'),  
    path('login/', views.login_view, name='login'),  
    path('logout/', views.logout_view, name='logout'),

    path('home/',views.home,name='home'), 
    path('profile/', views.profile_view, name='profile'),  
    path('edit-profile/', views.edit_profile_view, name='edit_profile'),  
    path('delete-profile/', views.delete_profile_view, name='delete_profile'),


    path('admin', views.admin, name='admin'), 
    path('viewusers',views.viewusers,name='viewusers'),

    path('addhall',views.add_hall,name='addhall'),
    path('edit-hall/<int:id>/', views.edit_hall, name='edithall'),
    path('delete-hall/<int:id>/', views.delete_hall, name='deletehall'),

    path('hall/<int:hall_id>/', views.hall_detail_view, name='hall_detail'),
    
    path('adddetails',views.hall_details,name='halldetails'),

    path('addfood',views.add_food,name='addfood'),
    path('fooddetails',views.food_details,name='fooddetails'),
    path('update_food/<int:food_id>/',views.update_food,name='update_food'),
    path('delete_food/<int:food_id>/',views.delete_food,name='delete_food'),

    path('resetpassword',views.password_reset_request,name='resetpassword'),
    path('verifyotp',views.verify_otp,name='verifyotp'),
    path('newpassword',views.set_new_password,name='newpassword'),

    path('adddecoration',views.add_decoration,name='adddecoration'),
    path('decorationdetails',views.decoration_details,name='decorationdetails'),
    path('updatedecoration/<int:id>',views.update_decoration,name='updatedecoration'),
    path('delete_decoration/<int:id>/', views.delete_decoration, name='delete_decoration'),


    path('booking_page',views.booking_page,name='booking_page'),
    path('booking_view',views.booking_view,name='booking_view'),
    path('admin_view_booking',views.admin_view_booking,name='admin_view_booking'),
    path('booking_detail/<int:id>/', views.booking_detail, name='booking_detail'),
    
    path('acceptrejectbooking/<int:id>',views.accept_reject_booking,name='acceptrejectbooking'),

    path('payment/<int:id>', views.stripe_payments, name='payment'),
    path('payment_status/<int:id>',views.payment_status,name='payment_status'),

    path('service',views.service,name='service'),
    path('about',views.about,name='about'),
    path('gallery',views.gallery,name='gallery'),
    path('testimonials',views.testimonials,name='testimonials'),
]
if settings.DEBUG:
    
   urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)