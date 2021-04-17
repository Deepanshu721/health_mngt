from django.shortcuts import render
from .models import Bed, BedType
from django.views import View

# Create your views here.
class StatusOfBed(View):
    def get(self, request):
        bed_list = Bed.get_all()
        context = {'bed_list':bed_list}
        if 'bed_no' in request.GET:
            bed_no = request.GET.get('bed_no')
            bed, patient = Bed.get_by_no(bed_no)
            print(patient)
            context['bed'] = bed
            if patient.exists():
                context['patient'] = patient[0].name
            else:
                context['patient'] = 'No patient'
    
        return render(request, 'bed/status.html', context)

class ListOfBeds(View):
    def get(self, request):
        context = {}
        if 'bed_status' in request.GET:
            bed_status = request.GET.get('bed_status')
            bed_list = Bed.get_list_by_status(bed_status)
            print(bed_list)
            context['bed_list'] = bed_list

        return render(request, 'bed/listofbeds.html', context)

 
class BedTypesStatus(View):
    def get(self, request):
        bedtypeslist = BedType.get_all()
        context = {'bedtypeslist':bedtypeslist}
        if 'bed_type' in request.GET:
            bed_type = request.GET.get('bed_type')
            print(bed_type)
            bed_status = Bed.get_bed_types_status(bed_type)
            context['bed_status'] = bed_status

        return render(request, 'bed/bedtypesstatus.html', context)
    