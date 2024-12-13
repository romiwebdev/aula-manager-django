from django.contrib import admin
from .models import RoomBooking
from django.contrib import admin
from .models import RoomBooking, RentalPrice
from django.utils.html import format_html

class RentalPriceAdmin(admin.ModelAdmin):
    list_display = ('day_type', 'price_per_hour')

class RoomBookingAdmin(admin.ModelAdmin):
    list_display = (
        'event_name', 
        'customer_name', 
        'start_time', 
        'end_time', 
        'is_paid',  # Menampilkan status pembayaran
        'is_approved',  # Menampilkan status persetujuan
        'payment_proof_preview',
    )
    
    list_filter = (
        'is_paid',  # Filter berdasarkan status pembayaran
        'is_approved',  # Filter berdasarkan status persetujuan
    )
    
    def payment_proof_preview(self, obj):
        return obj.payment_proof.url if obj.payment_proof else "No proof uploaded"

    
     # Menambahkan fitur untuk mengubah status is_approved di admin
    actions = ['approve_booking']

    def approve_booking(self, request, queryset):
        queryset.update(is_approved=True)
    approve_booking.short_description = "Setujui Pemesanan"


admin.site.register(RoomBooking, RoomBookingAdmin)
admin.site.register(RentalPrice, RentalPriceAdmin)


    
    
