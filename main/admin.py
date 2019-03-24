from django.contrib import admin
from .models import Pupil, Order, Event, Day

admin.site.register(Day)
admin.site.register(Pupil)
admin.site.register(Order)
admin.site.register(Event)