from django.db import models

# Create your models here.

# ilac tablosu
class Medicine(models.Model):
   
    ilac_adi = models.CharField(max_length = 50, verbose_name = 'İlaç İsmi')
    prospekt=models.TextField(max_length=200,null=True,verbose_name="Prospektüs")
    ilacfiyati=models.FloatField(null=True,verbose_name="İlaç Fiyatı")
    created_date = models.DateTimeField(auto_now = True, blank = True, verbose_name = 'Eklenme Tarihi')
    def __str__(self):
        return self.ilac_adi

class Patient(models.Model):
    
    first_name=models.CharField(max_length=30,verbose_name="İsim")
    last_name = models.CharField(max_length=30,verbose_name="Soyisim")
    mail=models.EmailField(max_length=50,verbose_name="Mail")
    created_date=models.DateTimeField(auto_now=True,verbose_name="Oluşturulma Tarihi")
    def __str__(self):
        return self.first_name

class Recete(models.Model):
    hasta=models.ForeignKey(Patient,null=True,on_delete=models.SET_NULL)
    created_date=models.DateTimeField(auto_now=True)
    tags=models.ManyToManyField(Medicine,verbose_name="İlaçlar")