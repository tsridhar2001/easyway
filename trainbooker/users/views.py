from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from bookings.models import ExpressTicket, LocalTicket, PlatformTicket

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def index_view(request):
    # Fetch the most recent bookings for the user
    express_bookings = ExpressTicket.objects.filter(user=request.user).order_by('-booked_at')[:5]  # Limit to 5 most recent
    local_bookings = LocalTicket.objects.filter(user=request.user).order_by('-booked_at')[:5]
    platform_bookings = PlatformTicket.objects.filter(user=request.user).order_by('-booked_at')[:5]

    # Combine bookings or pass separately as needed
    context = {
        'user': request.user,
        'express_bookings': express_bookings,
        'local_bookings': local_bookings,
        'platform_bookings': platform_bookings,
    }
    return render(request, 'users/index.html', context)
