from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # أضفنا 'status' هنا في النهاية 👇
    list_display = ('id', 'user', 'car', 'start_date', 'end_date', 'total_price', 'status')
    list_filter = ('status', 'created_at')
    # يجب أن يكون الحقل موجوداً في list_display ليكون قابلاً للتعديل
    list_editable = ('status',)