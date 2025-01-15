from django.urls import path
from . import views

app_name = 'scoreapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('scorecard/', views.scorecard, name='scorecard'),
    path('graphs/', views.graphs, name='graphs'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
   
    path('treeplanting/', views.treeplanting_form_view, name='treeplanting_form'),

]
