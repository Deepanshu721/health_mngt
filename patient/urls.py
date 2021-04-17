from django.urls import path
from . import views

urlpatterns = [
    path('add_patient', views.AddPatient.as_view(), name='add_patient'),
    path('get_patient', views.GetPatient.as_view(), name='get_patient'),
    path('discharge_patient', views.DischargePatient.as_view(), name='discharge_patient'),
]