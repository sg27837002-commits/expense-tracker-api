from django.contrib import admin
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'category', 'user', 'date')
    list_filter = ('category', 'date')
    search_fields = ('title', 'description', 'user__username')