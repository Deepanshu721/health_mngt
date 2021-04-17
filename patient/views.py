from django.shortcuts import render
from .forms import PatientForm
from bed.models import Bed, BedType
from .models import Patient
from django.views import View

# Create your views here.
class AddPatient(View):
    def get(self, request):
        bedtypeslist = BedType.get_all()
        context = {'bedtypeslist':bedtypeslist}
        form = PatientForm()
        context['form'] = form
        return render(request, 'patient/add_patient.html', context)

    def post(self, request):
        bedtypeslist = BedType.get_all()
        context = {'bedtypeslist':bedtypeslist}
        form = PatientForm(request.POST)
        if form.is_valid():
            bed_list = Bed.get_list_by_type(request.POST.get('bed_type'))
            if bed_list.exists():
                patient = form.save(commit=False)
                patient.bed = bed_list[0]
                patient.status = 'A'
                patient.save()
                Bed.update_status_to_A(bed_list[0].id)
                context['msg'] = "Patient added successfully"   
                form = PatientForm()
            else:
                context['msg'] = "No bed available as of now. Patient can't be added"    
        
        context['form'] = form
        return render(request, 'patient/add_patient.html', context)

class GetPatient(View):
    def get(self, request):
        bedtypeslist = BedType.get_all()
        context = {'bedtypeslist':bedtypeslist} 
        return render(request, 'patient/get_patient.html', context)

    def post(self, request):
        bedtypeslist = BedType.get_all()
        context = {'bedtypeslist':bedtypeslist} 
        patients_list = Patient.get_all_by_bed_type(request.POST.get('bed_type'))
        context['patients_list'] = patients_list
        return render(request, 'patient/get_patient.html', context)


class DischargePatient(View):
    def get(self, request):
        context = {} 
        return render(request, 'patient/discharge_patient.html', context)

    def post(self, request):
        context = {} 
        if request.method == 'POST':
            id = request.POST.get('id')
            patient = Patient.check_if_exist(id)
            if patient:
                Patient.discharge_patient(patient.id)
                print(patient.bed)
                Bed.update_status_to_E(patient.bed.id)
                context['msg'] = "Patient get discharged"
            else:
                context['msg'] = "No patient with this id"
        return render(request, 'patient/discharge_patient.html', context)
