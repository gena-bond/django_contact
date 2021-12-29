from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import JsonResponse

from .forms import *
from .models import Contact

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class ContactViews (View):
    """Список контактов"""
    def get(self, request):
        contacts = Contact.objects.all()
        return render(request, "contact/contact.html", {"contact_list": contacts})


def updatecontact(request, pk):
    """Обновление контактов"""
    contact = Contact.objects.get(id=pk)
    form = AddContactForm(request.POST or None, instance = contact)
    if form.is_valid():
        form.save()
        return  redirect('home')
    return render(request, "contact/updatecontact.html", {"contact": contact, 'form':form})


def addcontact(request):
    """Добавление контакта. Работает по url = /addcontact"""
    form = AddContactForm()
    if request.method == 'POST' and is_ajax(request=request):
        form = AddContactForm(request.POST)
        if form.is_valid():
            contact = form.cleaned_data['name']
            form.save()
            return  JsonResponse({"contact": contact}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)
    return render(request, "contact/addcontact.html", {'form': form})


