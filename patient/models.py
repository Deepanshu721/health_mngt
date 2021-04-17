from django.db import models
from bed.models import BedType, Bed

# Create your models here.
class Patient(models.Model):
    PATIENT_STATUS = (
        ('A', 'Assigned'),
        ('D', 'Discharged')
    )
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=PATIENT_STATUS)

    @staticmethod
    def check_if_exist(patient_id):
        patient = Patient.objects.filter(id=patient_id)
        if patient.exists():
            return patient[0]
        else:
            return False

    @staticmethod
    def get_by_id(patient_id):
        return Patient.objects.get(id=patient_id)

    @staticmethod
    def get_all_by_bed_type(bed_type_id):
        return Patient.objects.filter(bed__bedtype__id=bed_type_id)

    @staticmethod
    def discharge_patient(patient_id):
        return Patient.objects.filter(id=patient_id).update(status='D')
