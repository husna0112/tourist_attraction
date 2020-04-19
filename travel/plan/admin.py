from django.contrib import admin
from .models import Plan
# Register your models here.

class PlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'detail']
    list_per_page = 20
admin.site.register(Plan)