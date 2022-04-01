from django.contrib import admin
from .models import *



# Register your models here.

# medicine tablosu
@admin.register(Medicine)

class MedicineAdmin(admin.ModelAdmin):
    list_display=["ilac_adi","prospekt","created_date","ilacfiyati"]

    list_display_links=["ilac_adi"]

    search_fields=["ilac_adi"]
    list_filter=["created_date"]
    class Meta:
        
        model=Medicine

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display=["first_name","last_name","mail","created_date"]

    list_display_links=["first_name"]

    search_fields=["first_name"]
    list_filter=["created_date"]
    class Meta:
        
        model=Patient
@admin.register(Recete)
class ReceteAdmin(admin.ModelAdmin):
    list_display=["hasta","created_date"]

    list_display_links=["hasta"]

    search_fields=["hasta"]
    list_filter=["created_date"]
    class Meta:
        
        model=Recete,Patient,Medicine