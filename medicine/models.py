from django.db import models
from django.utils.safestring import mark_safe
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw

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
        return self.mail
    def __str__(self):
        return self.first_name

class Recete(models.Model):
    hasta=models.ForeignKey(Patient,null=True,on_delete=models.SET_NULL)
    created_date=models.DateTimeField(auto_now=True)
    tags=models.ManyToManyField(Medicine,verbose_name="İlaçlar")
    qr_code=models.ImageField(upload_to="qr_codes",blank=True)
    toplam=models.FloatField(null=True,blank=True,verbose_name="Tutar (TL)")
    ilaclar=models.CharField(max_length=100,null=True,blank=True,verbose_name="İlaçlar")

    def __str__(self):
        return self.hasta.first_name
        
    
    def get_ilacfiyati(self):
        total=0
        for i in self.tags.all():
            total=total + i.ilacfiyati
        return total

    def get_tags_values(self):
        ret = "<ul>"
        for i in self.tags.all():
            ret += "<li>"+ i.ilac_adi + "</li>"
        
        return mark_safe(ret[:-1])
    
    def get_tags_values2(self):
        ret=[]
        
        for i in self.tags.all():
            
            ret.append(i.ilac_adi)
        
        return ret
    

        
    
    def save(self,*args,**kwargs):

        super(Recete,self).save(*args,**kwargs)
        html=""
        for i in self.tags.all():
            html+=" "+ i.ilac_adi +" "
        self.ilaclar=html

        qrcode_img=qrcode.make(html)
        canvas=Image.new('RGB', (qrcode_img.pixel_size, qrcode_img.pixel_size), 'white')
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname=f'qr_code-{self.hasta}.png'
        buffer=BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname,File(buffer),save=False)
        canvas.close()

        total=0
        for i in self.tags.all():
            total=total + i.ilacfiyati
        self.toplam=total

        
        super(Recete,self).save(*args,**kwargs)

        
        

    
   


        
    