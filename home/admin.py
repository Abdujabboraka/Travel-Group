from django.contrib import admin
from .models import User, Destination, Booking, Review
# Register your models here.
admin.site.register(User)
admin.site.register(Destination)
admin.site.register(Booking)
admin.site.register(Review)