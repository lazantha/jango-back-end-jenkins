from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name='home-page'),
    path('contact/',views.contact,name='contact-page'),
    path('about/',views.about,name='about-page'),
]

