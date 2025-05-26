from django import forms
from .models import Feedback
from .models import CouponSubmission
from .models import Booking

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'rating', 'comments']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'date', 'time', 'guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }


    
class CouponForm(forms.ModelForm):
    class Meta:
        model = CouponSubmission
        fields = ['full_name', 'email', 'coupon_code', 'offer_name']
        widgets = {
            'coupon_code': forms.TextInput(attrs={'readonly': 'readonly'}),
            'offer_name': forms.TextInput(attrs={'readonly': 'readonly'}),
        }