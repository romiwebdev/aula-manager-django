



from django import forms
from .models import RentalPrice, RoomBooking
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


class RoomBookingForm(forms.ModelForm):
    class Meta:
        model = RoomBooking
        fields = [
            'event_name',
            'description',
            'start_time',
            'end_time',
            'customer_name',
            'phone_number',
            'organization',
            'rental_price',  # Field harga sewa yang diambil dari RentalPrice
            'email',
            'password',
            'payment_proof'
        ]
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Menambahkan pilihan harga berdasarkan model RentalPrice
        self.fields['rental_price'] = forms.ModelChoiceField(
            queryset=RentalPrice.objects.all(),
            empty_label="Harga Sewa",
            required=True
        )

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time and start_time >= end_time:
            raise ValidationError("Waktu mulai harus lebih awal daripada waktu selesai.")

        overlapping_bookings = RoomBooking.objects.filter(
            start_time__lt=end_time,
            end_time__gt=start_time
        )
        if overlapping_bookings.exists():
            raise ValidationError("Waktu yang dipilih sudah dipesan oleh pengguna lain. Silakan pilih waktu lain.")

        return cleaned_data

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.isdigit():
            raise forms.ValidationError("Nomor HP hanya boleh berisi angka.")
        return phone









    
    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.isdigit():
            raise forms.ValidationError("Nomor HP hanya boleh berisi angka.")
        return phone
