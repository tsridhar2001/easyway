from django.db import models
from django.contrib.auth.models import User

# ✅ Express Ticket Model
class ExpressTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    travel_date = models.DateField()
    passengers = models.IntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)
    train_name = models.CharField(max_length=64)
    travel_class = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.user.username} - Express: {self.source} to {self.destination}"

class LocalTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    line_direction = models.CharField(max_length=100)   
    travel_date = models.DateField()
    booked_at = models.DateTimeField(auto_now_add=True)
    ticket_count = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - ({self.line_direction}) x{self.ticket_count}"


from datetime import timedelta

class PlatformTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    station = models.CharField(max_length=100)
    ticket_count = models.PositiveIntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)

    @property
    def valid_until(self):
        # Valid for 6 hours from booking time (you can change this)
        return self.booked_at + timedelta(hours=6)

    def __str__(self):
        return f"{self.user.username} - Platform at {self.station} ({self.ticket_count})"
