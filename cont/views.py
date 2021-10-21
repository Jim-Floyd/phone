from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_safe

from cont.constants import PhoneType
from cont.models import Contact


@require_safe
def contact_list_page(request):
    contacts = Contact.objects.all()
    return render(request, 'list.html',{'contacts': contacts})


@require_safe
def details(request):
    return None


@require_safe
def create_page(request):
    choices = PhoneType.process()
    return render(request, 'create.html', {"choices": choices})


@require_POST
def create(request):
    return None


@require_safe
def delete_page(request):
    return None


@require_POST
def delete(request):
    return None