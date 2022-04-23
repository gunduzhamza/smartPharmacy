from django.shortcuts import render,redirect
from medicine.forms import *
from django.contrib import messages
from medicine.models import Medicine, Patient
from smartPharmacy import settings
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives
# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    medicines = Patient.objects.all()
    context={
        "medicines":medicines
    }
    return render(request,"dashboard.html",context)

def addpatient(request):
    form=PatientForm(request.POST or None)

    if form.is_valid():

        medicine=form.save(commit=False)
        medicine.first_name
        medicine.save()

        messages.success(request,"Hasta kaydı başarıyla oluşturuldu")
        return redirect("/medicines/dashboard/")

    return render(request,"addpatient.html",{"form":form})

def receteolustur(request):
    form=ReceteForm()
    if request.method=="POST":
        form=ReceteForm(request.POST)

        if form.is_valid():
            form.save()
            form.save()
            messages.success(request,"Reçete başarıyla oluşturuldu")
            return redirect("/medicines/dashboard/")

    context={"form":form}
    return render(request,"receteolustur.html",context)

def ilacListesi(request):
    ilaclar=Medicine.objects.all()
    context={
        "ilaclar":ilaclar
    }
    return render(request,"ilaclistesi.html",context)

def receteListesi(request):
    recete=Recete.objects.filter()

    
    
    context={
        "recete":recete,
        
    }
    return render(request,"recetelistesi.html",context)

def deTail(request,id):
    medicine= Recete.objects.filter(id=id).first()
    message= Recete.objects.filter(id=id)
    
    if request.method=="POST":
        mail= message.values_list('hasta__mail',flat=True).first()
        patient=message.values_list('hasta__first_name',flat=True).first()
        qr_code=message.values_list('qr_code',flat=True).first()
        
        filename = "C:/Users/gundu/OneDrive/Masaüstü/smartPharmacy/uploads/" + qr_code
        attachment = open(filename,'rb')

        msg = EmailMultiAlternatives(
            "Sayın "+ patient,
            'İlaçlarınızı eczane otomatına okutarak almayı unutmayınız.',
            settings.EMAIL_HOST_USER,
            [mail],
            headers={'Message-ID': 'foo'},
        )
        if attachment:
            mime_image = MIMEImage(attachment.read())
            mime_image.add_header('Content-ID', '<attachment>')
            msg.attach(mime_image)
       
        msg.send()

        messages.success(request,"mail başarıyla gönderildi")
        
        
        return redirect("/medicines/dashboard/")
    context={
        "medicine":medicine,
        
             }
        
    return render(request,"detail.html",context)
