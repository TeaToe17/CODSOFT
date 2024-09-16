from django.shortcuts import render, redirect , get_object_or_404

from .models import Contact
from .forms import ContactForm , SearchForm


def create_display_contacts(request):
    contacts = Contact.objects.all()
    search_form = SearchForm()
    form = ContactForm()
    results = []
    back = False

    if "query" in request.GET:
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            query = search_form.cleaned_data["query"]
            results = Contact.objects.filter(name__icontains=query) | Contact.objects.filter(number__icontains=query)
            back = True

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        
    context = {
        "contacts": contacts,
        "search": search_form,
        "results": results,
        "back": back,
        "form": form,
    }
    return render(request, "contacts.html", context)


def update_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    form = ContactForm(request.POST or None, instance=contact)

    if form.is_valid():
        form.save()
        return redirect("/")

    context = {"form": form}
    return render(request, "contacts.html", context)

def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    return redirect("/")

def search_contacts(request):
    search_form = SearchForm()
    results = []

    if "query" in request.GET:
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            query = search_form.cleaned_data["query"]
            results = Contact.objects.filter(name__icontains=query) | Contact.objects.filter(number__icontains=query)

    context = {
        "search": search_form,
        "results": results,
    }
    return render(request, "contacts.html", context)

"""
Pardon me for not following SRP (Single responsiblity principle) in implementing my views here.
I was curious about how this would turn out, so I implemented it.
"""
# def create_display_update_delete_search_contacts(request,id=None,delete=None):
#     OBJECTS = Contact.objects.all()
#     form = ContactForm()
#     search = SearchForm()
#     results = []
#     back = False

#     #Adding Contacts   
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = ContactForm()
#             return redirect("/")

#     #Updating Contacts
#     if id:
#         contact = Contact.objects.get(id=id)
#         form = ContactForm(request.POST or None,instance=contact)
#         if form.is_valid():
#             form.save()
#             return redirect("/")

#     #Deleting Contacts
#     if id and delete:
#         contact = Contact.objects.get(id=id)
#         contact.delete()
#         return redirect("/")

#     #Searching for Contacts based on name or phone_number 
#     if "query" in request.GET:
#         search = SearchForm(request.GET)
#         if search.is_valid():
#             query = search.cleaned_data["query"]
#             results = Contact.objects.filter(name__icontains=query) | Contact.objects.filter(number__icontains=query)
#             back = True

#     context ={
#         "contacts":OBJECTS,
#         "form":form,
#         "search":search,
#         "results":results,
#         "back":back,
#     }
#     return render(request,"contacts.html",context)