from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class UserProfile(models.Model):
    """Extended user model with role and additional information"""
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    phone = models.CharField(max_length=15, blank=True, null=True)
    room_no = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.role}"
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'


class Payment(models.Model):
    """Payment records for users"""
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('partial', 'Partial'),
        ('paid', 'Paid'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    month_year = models.CharField(max_length=7, help_text="Format: YYYY-MM")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    proof_image = models.ImageField(upload_to='payment_proofs/', blank=True, null=True)
    paid_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.month_year} - {self.status}"
    
    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        unique_together = ('user', 'month_year')
        ordering = ['-month_year', 'user__first_name']


class Grocery(models.Model):
    """Grocery item purchases"""
    CATEGORY_CHOICES = (
        ('vegetables', 'Vegetables'),
        ('grains', 'Grains'),
        ('dairy', 'Dairy'),
        ('spices', 'Spices'),
        ('other', 'Other'),
    )
    
    item_name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    quantity = models.CharField(max_length=50, help_text="e.g., 5 kg, 2 liters")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()
    month_year = models.CharField(max_length=7, help_text="Format: YYYY-MM")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.item_name} - {self.month_year}"
    
    class Meta:
        verbose_name = 'Grocery'
        verbose_name_plural = 'Groceries'
        ordering = ['-purchase_date']


class FixedExpense(models.Model):
    """Fixed monthly expenses"""
    month_year = models.CharField(max_length=7, unique=True, help_text="Format: YYYY-MM")
    kitchen_rent = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    maid_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    gas_cylinder = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    other_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    @property
    def total_fixed_expense(self):
        return self.kitchen_rent + self.maid_salary + self.gas_cylinder + self.other_expenses
    
    def __str__(self):
        return f"Fixed Expenses - {self.month_year}"
    
    class Meta:
        verbose_name = 'Fixed Expense'
        verbose_name_plural = 'Fixed Expenses'
        ordering = ['-month_year']


class Message(models.Model):
    """Messages from users to admin"""
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
    )
    
    MESSAGE_TYPE_CHOICES = (
        ('user', 'User Message'),
        ('system', 'System/Reminder'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    message_type = models.CharField(max_length=10, choices=MESSAGE_TYPE_CHOICES, default='user', help_text="Type of message")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)
    admin_reply = models.TextField(blank=True, null=True, help_text="Admin's response to this message")
    replied_at = models.DateTimeField(blank=True, null=True)
    user_reply = models.TextField(blank=True, null=True, help_text="User's response to admin reply")
    user_replied_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.subject}"
    
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['-created_at']


class MessSettings(models.Model):
    """Global mess settings"""
    max_users = models.IntegerField(default=50)
    current_month_year = models.CharField(max_length=7, default=datetime.now().strftime('%Y-%m'))
    upi_id = models.CharField(max_length=100, blank=True, null=True)
    upi_qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Mess Settings - {self.current_month_year}"
    
    class Meta:
        verbose_name = 'Mess Settings'
        verbose_name_plural = 'Mess Settings'


class MealPlan(models.Model):
    """Daily meal plan"""
    date = models.DateField(unique=True, help_text="Date for this meal plan")
    breakfast = models.TextField(blank=True, null=True, help_text="Breakfast menu")
    lunch = models.TextField(blank=True, null=True, help_text="Lunch menu")
    dinner = models.TextField(blank=True, null=True, help_text="Dinner menu")
    notes = models.TextField(blank=True, null=True, help_text="Additional notes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Meal Plan - {self.date}"
    
    class Meta:
        verbose_name = 'Meal Plan'
        verbose_name_plural = 'Meal Plans'
        ordering = ['-date']
