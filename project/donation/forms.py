from django import forms  
from donation.models import Donation
from django.forms import fields

class DonationForm(forms.ModelForm):  
    class Meta:  
        model = Donation  
        fields = "__all__"  