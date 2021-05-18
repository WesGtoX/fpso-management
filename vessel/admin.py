from django.contrib import admin
from vessel.models import Vessel


@admin.register(Vessel)
class VesselAdmin(admin.ModelAdmin):
    list_display = ('code',)
    list_filter = ('code',)
    search_fields = ('code',)
