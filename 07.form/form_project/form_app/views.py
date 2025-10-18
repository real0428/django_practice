from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def home_view(request):
  return render(request, 'form_app/home.html')

def contact_view(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      form.send_email()
      return redirect('contact-success')
  else:
    form = ContactForm()
    return render(request, 'form_app/contact.html', {'form': form})

def contact_success_view(reqeust):
  return render(reqeust, 'form_app/contact-success.html')



