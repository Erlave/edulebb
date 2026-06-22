from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name", "email", "rate", "comment"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "نام و نام خانوادگی"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "آدرس ایمیل"
            }),

            "rate": forms.Select(
                choices=[(i, i) for i in range(1, 6)],
                attrs={"class": "form-control"}
            ),

            "comment": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "اینجا پیام خود را بنویسید..."
            })
        }