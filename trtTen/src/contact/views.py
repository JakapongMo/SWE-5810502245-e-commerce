from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm

# Create your views here.
def contact(request):
    title = "Contact"
    form = contactForm(request.POST or None)
    context = {'title': title, 'form':form,}
    confirm_massage =None

    if form.is_valid():
    #    print form.cleaned_data['email']
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Massage from MYSITE.com'
        message = '{0} {1}'.format(comment, name)
        emailForm = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail( subject , message, emailForm, emailTo, fail_silently= True)
        title = "Thaanks!"
        confirm_massage = "Thaanks for the Massage. We will get right back to you."
        form = None
    #context = locals()
    context = {'title': title,'form': form ,'confirm_massage' : confirm_massage, }
    template = 'contact.html'
    return render(request,template,context)
