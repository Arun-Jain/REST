from django.contrib import admin
from .models import Casino
# Register your models here.
@admin.register(Casino)
class CasinoAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'address', 'created_at', 'modified_at']
