from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import ContactForm
# Create your views here.





def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "پیام شما با موفقیت ارسال شد."
            )

            return redirect("contact")

    else:
        form = ContactForm()

    return render(
        request,
        "contact_us/contact.html",
        {
            "form": form
        }
    )