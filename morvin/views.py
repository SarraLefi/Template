from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.views import PasswordSetView,PasswordChangeView
from django.urls import reverse_lazy

# class Index(LoginRequiredMixin,TemplateView):
class Index(TemplateView):
    template_name = "index.html"
class Calendar(TemplateView):
    template_name = "calendar.html"
class Chat(TemplateView):
    template_name = "chat.html"
class MyPasswordChangeView( PasswordChangeView):
    success_url = reverse_lazy('index')
class MyPasswordSetView( PasswordSetView):
    success_url = reverse_lazy('index')