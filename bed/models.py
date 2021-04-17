from django.db import models

# Create your models here.
class BedType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all():
        return BedType.objects.all()
    
        

class Bed(models.Model):
    BED_STATUS = (
        ('A', 'Assigned'),
        ('E', 'Empty')
    )
    bedtype = models.ForeignKey(BedType, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=BED_STATUS)

    
    @staticmethod
    def get_all():
        return Bed.objects.all()
    
    @staticmethod
    def get_by_no(bed_no):
        bed = Bed.objects.get(id=bed_no)
        patient = bed.patient_set.filter(status='A')
        return (bed, patient)

    @staticmethod
    def get_list_by_status(status):
        if status == 'E':
            return Bed.objects.filter(status='E')
        else:
            return Bed.objects.filter(status='A')

    @staticmethod
    def get_list_by_type(bed_type_id):
        return Bed.objects.filter(bedtype__id=bed_type_id, status='E')

    @staticmethod
    def get_bed_types_status(bed_type_id):
        data = Bed.objects.filter(status='E', bedtype__id=bed_type_id)
        if len(data)==0:
            return 'Full'
        else:
            return 'Empty'

    @staticmethod
    def update_status_to_A(bed_id):
        return Bed.objects.filter(id=bed_id).update(status='A')

    @staticmethod
    def update_status_to_E(bed_id):
        return Bed.objects.filter(id=bed_id).update(status='E')