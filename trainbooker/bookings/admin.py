from django.contrib import admin

# Register your models here.
from .models import ExpressTicket, LocalTicket, PlatformTicket

admin.site.register(ExpressTicket)
admin.site.register(LocalTicket)
admin.site.register(PlatformTicket)