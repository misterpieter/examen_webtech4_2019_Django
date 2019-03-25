# OPDRACHT:
# Make a WebService in Django that returns the number of hours, minutes and seconds 
# that remain until the official Brexit date.
# take place on 29 March 2019 at 11 pm UK time.



from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
