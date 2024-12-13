from datetime import datetime
from django.shortcuts import render, redirect
from .models import RoomBooking
from .forms import RoomBookingForm
from django.http import HttpResponseForbidden

# Tampilkan daftar pemesanan yang sudah di-approve saja
def room_booking_list(request):
    # Ambil waktu sekarang
    now = datetime.now()

    # Hanya tampilkan pemesanan yang waktu selesai-nya lebih besar dari waktu sekarang dan sudah di-approve
    bookings = RoomBooking.objects.filter(end_time__gt=now, is_approved=True)

    return render(request, 'room_booking_list.html', {'bookings': bookings})

# Form untuk membuat pemesanan baru
from django.contrib import messages

def room_booking_create(request):
    if request.method == 'POST':
        form = RoomBookingForm(request.POST, request.FILES)  # Pastikan menerima `FILES` untuk payment proof
        if form.is_valid():
            booking = form.save(commit=False)
            booking.status = 'PENDING'  # Set status default
            booking.is_approved = False  # Belum di-approve
            booking.save()
            messages.success(request, "Pesanan Anda telah dibuat. Silakan tunggu persetujuan dari admin. Jika sudah disetujui, pesanan Anda akan tampil di halaman daftar.")
            return redirect('room_booking_list')
    else:
        form = RoomBookingForm()
    return render(request, 'room_booking_form.html', {'form': form})



def verify_email_password(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        password = request.GET.get('password')

        # Cari pemesanan berdasarkan email dan password yang dimasukkan
        bookings = RoomBooking.objects.filter(email=email, password=password)

        if bookings.exists():
            # Jika ditemukan, tampilkan daftar pesanan yang bisa diubah
            return render(request, 'booking_edit_form.html', {'bookings': bookings, 'email': email, 'password': password})
        else:
            return HttpResponseForbidden("Email atau password tidak valid.")

    return redirect('room_booking_list')

def room_booking_edit(request, pk):
    booking = RoomBooking.objects.get(pk=pk)
    if request.method == 'POST':
        form = RoomBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('room_booking_list')
    else:
        form = RoomBookingForm(instance=booking)
    return render(request, 'room_booking_edit.html', {'form': form, 'booking': booking})

from django.http import HttpResponseForbidden

def room_booking_cancel(request, pk):
    booking = RoomBooking.objects.get(pk=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('room_booking_list')
    return HttpResponseForbidden("Permintaan tidak valid.")



