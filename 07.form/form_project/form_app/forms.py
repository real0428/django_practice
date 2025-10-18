from django import forms

class ContactForm(forms.Form):
  name = forms.CharField(max_length=100)
  email = forms.EmailField()
  message = forms.CharField(widget=forms.Textarea)

  def send_email(self):
    clean_data = self.cleaned_data
    print(f"Sending email from {clean_data['email']} with message: {clean_data['message']}")