from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100)
    email = forms.EmailField(label="Your email")
    message = forms.CharField(label="Your message", widget=forms.Textarea)

    def send_email(self):
        print(
            f"Sending email from {self.cleaned_data['email']} with message {self.cleaned_data['message']}"
        )
