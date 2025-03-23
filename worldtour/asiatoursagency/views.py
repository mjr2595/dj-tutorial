from django.shortcuts import redirect, render

from .form import ContactForm
from .models import Tour


# Create your views here.
def home_view(request):
    tours = Tour.objects.all()
    context = {"tours": tours}
    return render(request, "tours/home.html", context)


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect("contact-success")
    else:
        form = ContactForm()
    context = {"form": form}
    return render(request, "tours/contact.html", context)


def contact_success_view(request):
    return render(request, "tours/contact_success.html")
