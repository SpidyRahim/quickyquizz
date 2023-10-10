from .models import Profile
from django import forms
from .models import StudentReview


class StudentReviewForm(forms.ModelForm):
    class Meta:
        model = StudentReview
        fields = ['rating']


# notun


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # Include the fields you want to allow students to update
        fields = ['user', 'email',]
