from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model_name', 'daily_price', 'created_at')
    list_filter = ('brand',) # تأكد من وجود الفاصلة لأنها Tuple
    search_fields = ('brand', 'model_name')