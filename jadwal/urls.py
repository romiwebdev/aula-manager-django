from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.room_booking_list, name='room_booking_list'),  # Home
    path('create/', views.room_booking_create, name='room_booking_create'),  # Booking form
    path('verify/', views.verify_email_password, name='verify_email_password'),
    path('edit/<int:pk>/', views.room_booking_edit, name='room_booking_edit'),
    path('cancel/<int:pk>/', views.room_booking_cancel, name='room_booking_cancel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

