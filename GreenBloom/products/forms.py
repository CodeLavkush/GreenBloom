from django import forms

class FilterForm(forms.Form):
    CATEGORY_CHOICES = [
        ('ALL', 'All Categories'),  # Optional default
        ('HP', 'Highted Pot'),
        ('SM', 'Small Pot'),
        ('FP', 'Fat Pot'),
    ]

    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"})
    )
