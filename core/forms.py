from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Payment, Grocery, FixedExpense, Message


class UserRegistrationForm(UserCreationForm):
    """Form for creating new users by admin"""
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    room_no = forms.CharField(max_length=20, required=True)
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES, initial='user')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            # Create user profile
            UserProfile.objects.create(
                user=user,
                role=self.cleaned_data['role'],
                phone=self.cleaned_data['phone'],
                room_no=self.cleaned_data['room_no']
            )
        return user


class UserEditForm(forms.ModelForm):
    """Form for editing existing users"""
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    room_no = forms.CharField(max_length=20, required=True)
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            profile = self.instance.userprofile
            self.fields['phone'].initial = profile.phone
            self.fields['room_no'].initial = profile.room_no
            self.fields['role'].initial = profile.role


class PaymentForm(forms.ModelForm):
    """Form for payment management"""
    class Meta:
        model = Payment
        fields = ['user', 'month_year', 'amount', 'status', 'transaction_id', 'proof_image']
        widgets = {
            'month_year': forms.TextInput(attrs={'type': 'month'}),
            'amount': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }


class UserPaymentForm(forms.ModelForm):
    """Form for user payment submission"""
    class Meta:
        model = Payment
        fields = ['transaction_id', 'proof_image']
        widgets = {
            'transaction_id': forms.TextInput(attrs={'placeholder': 'Enter UPI/Bank transaction ID'}),
        }


class GroceryForm(forms.ModelForm):
    """Form for grocery management"""
    class Meta:
        model = Grocery
        fields = ['item_name', 'category', 'quantity', 'price', 'purchase_date', 'month_year']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'month_year': forms.TextInput(attrs={'type': 'month'}),
            'price': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }


class FixedExpenseForm(forms.ModelForm):
    """Form for fixed expense management"""
    class Meta:
        model = FixedExpense
        fields = ['month_year', 'kitchen_rent', 'maid_salary', 'gas_cylinder', 'other_expenses']
        widgets = {
            'month_year': forms.TextInput(attrs={'type': 'month'}),
            'kitchen_rent': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'maid_salary': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'gas_cylinder': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'other_expenses': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }


class MessageForm(forms.ModelForm):
    """Form for users to send messages"""
    class Meta:
        model = Message
        fields = ('subject', 'message')
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': 'Enter subject'}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter your message'}),
        }


class AdminReplyForm(forms.ModelForm):
    """Form for admin reply to user messages"""
    class Meta:
        model = Message
        fields = ['admin_reply']
        widgets = {
            'admin_reply': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Type your reply here...'}),
        }
        labels = {
            'admin_reply': 'Reply to User'
        }
