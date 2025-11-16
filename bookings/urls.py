# bookings/urls.py
#from django.urls import path
#from . import views

#urlpatterns = [
 #booking-page
  #  path('create/<int:destination_id>/', views.create_booking, name='create_booking')
#]

from django.urls import path
from . import views

urlpatterns = [
    path('booking-page/', views.booking_page, name='booking_page'),
    path('create/<int:destination_id>/', views.create_booking, name='create_booking'),
]
