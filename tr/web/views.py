from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contacts.html")

def faq(request):
    return render(request, "faq.html")

def feature(request):
    return render(request, "features.html")

def integration(request):
    return render(request, "integrations.html")

def testimonials(request):
    return render(request, "testimonials.html")

def pricing(request):
    return render(request, "pricing.html")
