from django.urls import path
from layouts import views
urlpatterns = [
    ############### Layout ###############
    # Vertical
   
    path('layout_iconsidebar', views.IconSidebar.as_view(),name='layout_iconsidebar'),
   

]