from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from core.forms import ContactForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView

from core.tasks import my_task

def export(request):
    # my_task()
    my_task.delay()
    return HttpResponse('Exporting...')


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')



class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:contact')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.add_message(self.request, messages.SUCCESS, _('Your message has been sent successfully!'))
        return super().form_valid(form)
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        messages.add_message(self.request, messages.ERROR, _('Your message has not been sent!'))
        return super().form_invalid(form)



def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _('Your message has been sent successfully!'))
            return redirect(reverse_lazy('core:contact'))
        else:
            messages.add_message(request, messages.ERROR, _('Your message has not been sent!'))

    context = {
        'form': form
    }
    return render(request, 'contact.html', context=context)

