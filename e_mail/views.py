from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class EmailInbox(TemplateView):
    template_name = "email/email-inbox.html"
class EmailRead(TemplateView):
    template_name = "email/email-read.html"
class EmailCompose(TemplateView):
    template_name = "email/email-compose.html"