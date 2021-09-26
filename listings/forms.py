from django import forms 
from .models import Listings

class ListingsForm(forms.ModelForm):
    class Meta:
        model = Listings

        fields = [
            "name",
            "institution",
            "address",
            "description",
            "start_time",
            "close_time"
        ]