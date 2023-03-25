from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
############ Layout ############
# Vertical

class IconSidebar(TemplateView):
    template_name = "layouts/vertical/layouts-icon-sidebar.html"
