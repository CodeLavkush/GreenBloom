from django.shortcuts import render
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            print(f"Name: {name}, Email: {email}, Message: {message}")

            return render(request, 'contact.html', {"form" : form}) 
    else:
        form = ContactForm()
    return render(request, 'contact.html', {"form" : form})