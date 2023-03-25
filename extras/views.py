from django.shortcuts import render
from .models import Login
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Timeline(TemplateView):
    template_name = "extras/pages/pages-timeline.html"
class Invoice(TemplateView):
    template_name = "extras/pages/pages-invoice.html"
class Blankpage(TemplateView):
    template_name = "extras/pages/pages-blank.html"
class Error404(TemplateView):
    template_name = "extras/pages/pages-404.html"
class Error500(TemplateView):
    template_name = "extras/pages/pages-500.html"
class Pricing(TemplateView):
    template_name = "extras/pages/pages-pricing.html"
class Maintenance(TemplateView):
    template_name = "extras/pages/pages-maintenance.html"
class Comingsoon(TemplateView):
    template_name = "extras/pages/pages-comingsoon.html"
class Faqs(TemplateView):
    template_name = "extras/pages/pages-faq.html"
class Lockscreen(TemplateView):
    template_name = "authentication/auth-lock-screen.html"
class Login(TemplateView):
    template_name = "authentication/auth-login.html"
def login (request):
    log=login.objects.all()
    context = {"log":log,}
    return render(request,"login.html" ,context)
class Register(TemplateView):
    template_name = "authentication/auth-register.html"