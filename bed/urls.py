from django.urls import path
from . import views

urlpatterns = [
    path('statusofbed', views.StatusOfBed.as_view(), name='statusofbed'),
    path('listofbeds', views.ListOfBeds.as_view(), name='listofbeds'),
    path('bedtypesstatus', views.BedTypesStatus.as_view(), name='bedtypesstatus'),
]