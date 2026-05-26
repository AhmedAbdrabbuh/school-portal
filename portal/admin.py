from django.contrib import admin
from .models import Payment

# Register your models here.

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'date', 'description')
    list_filter = ('date', 'user')
    search_fields = ('user__username', 'description')
