from django.contrib import admin

# Register your models here.
from .models import talks,notifications,employess

admin.site.register(talks)
admin.site.register(notifications)
admin.site.register(employess)