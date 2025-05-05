from django.db import models
from django.contrib.auth.models import User

# ✅ Express Ticket Model
class ExpressTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_station = models.CharField(max_length=100)
    to_station = models.CharField(max_length=100)
    travel_date = models.DateField()
    passengers = models.IntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Express: {self.from_station} to {self.to_station}"

class LocalTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    line = models.CharField(max_length=100)        # e.g. "Beach–Tambaram"
    direction = models.CharField(max_length=100)   # e.g. "Toward Tambaram"
    travel_date = models.DateField()
    quantity = models.IntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.line} ({self.direction}) x{self.quantity}"


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
