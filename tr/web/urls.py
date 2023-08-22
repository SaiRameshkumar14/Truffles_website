from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.index, name="Home"),
    path("faq/", views.faq, name="faq"),
    path("contact/", views.contact, name="contact"),
    path("features/", views.feature, name="features"),
    path("integrations/", views.integration, name="integrations"),
    path("testimonials/", views.testimonials, name="testimonials"),

]