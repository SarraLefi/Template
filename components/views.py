from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
############ Components ############
# UI Elements 
class Alerts(TemplateView):
    template_name = "components/ui_elements/ui-alerts.html"
class Buttons(TemplateView):
    template_name = "components/ui_elements/ui-buttons.html"
class Cards(TemplateView):
    template_name = "components/ui_elements/ui-cards.html"
class Carousel(TemplateView):
    template_name = "components/ui_elements/ui-carousel.html"
class Colors(TemplateView):
    template_name = "components/ui_elements/ui-colors.html"
class Dropdowns(TemplateView):
    template_name = "components/ui_elements/ui-dropdowns.html"
class Generals(TemplateView):
    template_name = "components/ui_elements/ui-general.html"
class Grid(TemplateView):
    template_name = "components/ui_elements/ui-grid.html"
class Images(TemplateView):
    template_name = "components/ui_elements/ui-images.html"
class Lightbox(TemplateView):
    template_name = "components/ui_elements/ui-lightbox.html"
class Modals(TemplateView):
    template_name = "components/ui_elements/ui-modals.html"
class Progressbars(TemplateView):
    template_name = "components/ui_elements/ui-progressbars.html"
class Rangeslider(TemplateView):
    template_name = "components/ui_elements/ui-rangeslider.html"
class Rating(TemplateView):
    template_name = "components/ui_elements/ui-rating.html"
class SessionTimeout(TemplateView):
    template_name = "components/ui_elements/ui-session-timeout.html"
class SweetAlert(TemplateView):
    template_name = "components/ui_elements/ui-sweet-alert.html"
class TabsAccordions(TemplateView):
    template_name = "components/ui_elements/ui-tabs-accordions.html"
class Typography(TemplateView):
    template_name = "components/ui_elements/ui-typography.html"
class Video(TemplateView):
    template_name = "components/ui_elements/ui-video.html"

# Forms
class Elements(TemplateView):
    template_name = "components/forms/form-elements.html"
class Validation(TemplateView):
    template_name = "components/forms/form-validation.html"
class Advanced(TemplateView):
    template_name = "components/forms/form-advanced.html"
class Editors(TemplateView):
    template_name = "components/forms/form-editors.html"
class Upload(TemplateView):
    template_name = "components/forms/form-uploads.html"
class Xeditable(TemplateView):
    template_name = "components/forms/form-xeditable.html"
class Wizard(TemplateView):
    template_name = "components/forms/form-wizard.html"
class Mask(TemplateView):
    template_name = "components/forms/form-mask.html"

# Charts
class Apex(TemplateView):
    template_name = "components/charts/charts-apex.html"
class Chartist(TemplateView):
    template_name = "components/charts/charts-chartist.html"
class Chartjs(TemplateView):
    template_name = "components/charts/charts-chartjs.html"
class Flot(TemplateView):
    template_name = "components/charts/charts-flot.html"
class Knob(TemplateView):
    template_name = "components/charts/charts-knob.html"
class Sparkline(TemplateView):
    template_name = "components/charts/charts-sparkline.html"

#API
class API(TemplateView):
    template_name = "components/API/API.html"

# Tables
class Personnes(TemplateView):
    template_name = "components/contacts/personnes.html"
class Organisations(TemplateView):
    template_name = "components/contacts/organisations.html"


# Icons
class Dripicons(TemplateView):
    template_name = "components/icons/icons-dripicons.html"
class Fontawesome(TemplateView):
    template_name = "components/icons/icons-fontawesome.html"
class Materialdesign(TemplateView):
    template_name = "components/icons/icons-materialdesign.html"
class Themify(TemplateView):
    template_name = "components/icons/icons-themify.html"

# Maps
class Google(TemplateView):
    template_name = "components/maps/maps-google.html"
class Vector(TemplateView):
    template_name = "components/maps/maps-vector.html"