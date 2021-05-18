from django.contrib import admin
from .models import Vessel


@admin.register(Vessel)
class VesselAdmin(admin.ModelAdmin):
    list_display = ('code',)
    list_filter = ('code',)
    search_fields = ('code',)
