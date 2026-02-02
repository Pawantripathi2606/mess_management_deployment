from django.contrib import admin
from .models import UserProfile, Payment, Grocery, FixedExpense, Message, MessSettings, MealPlan


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone', 'room_no', 'is_active')
    list_filter = ('role', 'is_active')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'phone', 'room_no')
    ordering = ('-created_at',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'month_year', 'amount', 'status', 'paid_date', 'transaction_id')
    list_filter = ('status', 'month_year', 'paid_date')
    search_fields = ('user__username', 'user__first_name', 'transaction_id')
    ordering = ('-created_at',)


@admin.register(Grocery)
class GroceryAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'category', 'quantity', 'price', 'purchase_date', 'month_year')
    list_filter = ('category', 'month_year', 'purchase_date')
    search_fields = ('item_name',)
    ordering = ('-created_at',)


@admin.register(FixedExpense)
class FixedExpenseAdmin(admin.ModelAdmin):
    list_display = ('month_year', 'kitchen_rent', 'maid_salary', 'gas_cylinder', 'other_expenses', 'total_fixed_expense')
    list_filter = ('month_year',)
    ordering = ('-month_year',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'status', 'created_at', 'resolved_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'subject', 'message')
    ordering = ('-created_at',)


@admin.register(MessSettings)
class MessSettingsAdmin(admin.ModelAdmin):
    list_display = ('current_month_year', 'max_users', 'upi_id', 'updated_at')


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('date', 'breakfast', 'lunch', 'dinner')
    list_filter = ('date',)
    search_fields = ('breakfast', 'lunch', 'dinner', 'notes')
    ordering = ('-date',)
