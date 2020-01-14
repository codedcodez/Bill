from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
import time

from .forms import ContactForm, MobilewebForm
from .models import SoftwareTwoFifty, SoftwareFiveHundred, SoftwareSevenFifty, AddressUpload

def index(request):
    software_one = SoftwareTwoFifty.objects.all()
    software_two = SoftwareFiveHundred.objects.all()
    software_three = SoftwareSevenFifty.objects.all()
    wallet = AddressUpload.objects.all()

    context = {
        'software_one': software_one,
        'software_two': software_two,
        'software_three': software_three,
        'wallet': wallet,
    }
    return render(request, 'billsites/index.html', context)


class AboutView(TemplateView):
    template_name = 'billsites/about.html'


class TermsView(TemplateView):
    template_name = 'billsites/terms.html'


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']

            try:
                send_mail(subject, (message + "\n\nMessage sent by " + email), email, [settings.EMAIL_HOST_USER], fail_silently=False)
                messages.success(request, 'Message submitted successfully!')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('billsites:index')

    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form
    }

    return render(request, 'billsites/contact.html', context)


class TestView(TemplateView):
    template_name = 'billsites/test.html'


def mobile_software(request):
    if request.method == 'POST':
        mobile_form = MobilewebForm(data=request.POST)

        if mobile_form.is_valid():
            username = mobile_form.cleaned_data['username']
            wallet = mobile_form.cleaned_data['wallet']
            country = mobile_form.cleaned_data['country']
            key = mobile_form.cleaned_data['key']

            # form = mobile_form.save(commit=False)

            check_user = request.user.username
            if check_user == 'Successmaker4all':
                form = mobile_form.save()
                time.sleep(90)
                return HttpResponse("Congratulations! <br>Your mining has just begun, please check your bitcoin wallet after 48 hours for the generated 1 btc.<br><br>Thank you.")
            else:
                return HttpResponse("You are not a valid user.")

    else:
        mobile_form = MobilewebForm()

    context = {
        'mobile_form': mobile_form
    }

    return render(request, 'billsites/mobile_software.html', context)
