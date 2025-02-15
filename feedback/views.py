from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import FeedbackForm
from menu.models import Menu
from django.contrib import messages


def contact_us(request):
    template = loader.get_template('contact_us/contact-us.html')
    section = Menu.objects.all()
    context = {'form': FeedbackForm, 'section': section}
    if request.method == 'POST':
        fdbk = FeedbackForm(request.POST)
        if fdbk.is_valid:
            fdbk.save()
            messages.add_message(request, messages.INFO, "Сообщение успешно отправлено")
            return HttpResponse(template.render(context, request))
        else:
            pass
    else:
        return HttpResponse(template.render(context, request))
