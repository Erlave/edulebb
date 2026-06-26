from django import forms
from .models import BlogComment


class BlogCommentForm(forms.ModelForm):

    class Meta:
        model = BlogComment

        fields = (
            "name",
            "email",
            "subject",
            "message",
        )

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "نام"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "ایمیل"
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "موضوع"
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "نظر شما..."
                }
            )
        }