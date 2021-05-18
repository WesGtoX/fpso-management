from django.contrib import admin
from equipment.models import Equipment


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'location', 'status', 'vessel')
    list_filter = ('name', 'code', 'status')
    search_fields = ('name', 'code', 'location', 'status')
