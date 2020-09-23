from django.contrib import admin
from .models import Destination


class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name','price','offer')
admin.site.register(Destination,DestinationAdmin)

# Register your models here.
