from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm
# Create your views here.
def contact(request):
    form = contactForm(request.POST or None)

    if form.is_valid():
    #    print form.cleaned_data['email']
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Massage from MYSITE.com'
        message = '{0} {1}'.format(comment, name)
        emailForm = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail( subject , message, emailForm, emailTo, fail_silently= True)
    context = locals()
    template = 'contact.html'
    return render(request,template,context)
