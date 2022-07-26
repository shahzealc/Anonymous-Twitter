from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/',views.about),
    path('add_form/',views.show_form),
]