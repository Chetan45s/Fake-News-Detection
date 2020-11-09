from django.contrib import admin
from django.urls import path
from . import views 
from django.views.generic.base import RedirectView
from process.views import InputView

urlpatterns = [
    path('home/',views.home, name = 'home'),
    path('home/result',views.InputView, name = 'input'),
    path('',RedirectView.as_view(url='home/')),
]