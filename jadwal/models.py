from django.db import models

class RentalPrice(models.Model):
    DAY_CHOICES = [
        ('weekday', 'Senin - Jumat'),
        ('weekend', 'Sabtu - Minggu'),
    ]
    day_type = models.CharField(max_length=10, choices=DAY_CHOICES)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.get_day_type_display()} - {self.price_per_hour} IDR per hour'

class RoomBooking(models.Model):
    event_name = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    organization = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    rental_price = models.ForeignKey(RentalPrice, on_delete=models.SET_NULL, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    payment_proof = models.ImageField(upload_to='payment_proofs/', null=True, blank=True)

    def __str__(self):
        return f'Booking {self.event_name} by {self.customer_name}'

