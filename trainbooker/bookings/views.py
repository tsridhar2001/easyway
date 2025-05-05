from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ExpressTicketForm, LocalTicketForm, PlatformTicketForm

@login_required
def book_express_ticket(request):
    if request.method == 'POST':
        form = ExpressTicketForm(request.POST)
        if form.is_valid():
            express_ticket = form.save(commit=False)
            express_ticket.user = request.user
            express_ticket.save()
            return redirect('express_booking_success')
    else:
        form = ExpressTicketForm()
    return render(request, 'bookings/book_express.html', {'form': form})

@login_required
def express_booking_success(request):
    return render(request, 'bookings/express_success.html')

@login_required
def book_local_ticket(request):
    if request.method == 'POST':
        form = LocalTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('booking_success')
    else:
        form = LocalTicketForm()
    return render(request, 'bookings/book_local.html', {'form': form})

@login_required
def book_platform_ticket(request):
    if request.method == 'POST':
        form = PlatformTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('booking_success')
    else:
        form = PlatformTicketForm()
    return render(request, 'bookings/book_platform.html', {'form': form})

@login_required
def view_bookings(request):
    express_tickets = ExpressTicket.objects.filter(user=request.user).order_by('-booked_at')
    local_tickets = LocalTicket.objects.filter(user=request.user).order_by('-booked_at')
    platform_tickets = PlatformTicket.objects.filter(user=request.user).order_by('-booked_at')

    context = {
        'express_tickets': express_tickets,
        'local_tickets': local_tickets,
        'platform_tickets': platform_tickets,
    }
    return render(request, 'bookings/view_bookings.html', context)
