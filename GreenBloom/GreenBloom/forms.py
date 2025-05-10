from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder" : "Name", "required" : True}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={"placeholder" : "Email", "required" : True}))
    message = forms.CharField(max_length=100, widget=forms.Textarea(attrs={"placeholder" : "Message", "required" : True}))

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Name cannot contain numbers.")
        return name
    