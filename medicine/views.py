from django.shortcuts import render,redirect
from medicine.forms import *
from django.contrib import messages
from medicine.models import Medicine, Patient
from smartPharmacy import settings
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives
from django.forms import inlineformset_factory
from django import forms
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required
from pathlib import Path

# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required(login_url="user:login")
def dashboard(request):
    
    keyword=request.GET.get("keyword")
    if keyword:
        patient=Patient.objects.filter(first_name__contains=keyword)
        return render(request,"dashboard.html",{"patient":patient})
    
    medicines = Patient.objects.all()
    context={
        "medicines":medicines
    }
    return render(request,"dashboard.html",context)

@login_required(login_url="user:login")
def addpatient(request):
    form=PatientForm(request.POST or None)

    if form.is_valid():

        medicine=form.save(commit=False)
        medicine.first_name
        medicine.save()

        messages.success(request,"Hasta kaydı başarıyla oluşturuldu")
        return redirect("/medicines/dashboard/")

    return render(request,"addpatient.html",{"form":form})

@login_required(login_url="user:login")
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

@login_required(login_url="user:login")
def makeRecete(request,id):
    ReceteFormSet= inlineformset_factory(Patient,Recete,fields=('tags',),widgets={'tags': forms.CheckboxSelectMultiple()})

    hasta=Patient.objects.filter(id=id).first()
    formset=ReceteFormSet(instance=hasta)
    #form=ReceteForm2(initial={'hasta':hasta})

    if request.method=="POST":
        #form=ReceteForm2(request.POST)
        formset=ReceteFormSet(request.POST,instance=hasta)
        if formset.is_valid():
            formset.save()
            formset.save()
            messages.success(request,"Reçete başarıyla oluşturuldu")
            return redirect("/medicines/dashboard/")

    context={
        "formset":formset
    }
    return render(request,"makeRecete.html",context)

@login_required(login_url="user:login")    
def ilacListesi(request):
    ilaclar=Medicine.objects.all()
    context={
        "ilaclar":ilaclar
    }
    return render(request,"ilaclistesi.html",context)



@login_required(login_url="user:login")
def receteListesi(request):
    recete=Recete.objects.filter()

    
    
    context={
        "recete":recete,
        
    }
    return render(request,"recetelistesi.html",context)


@login_required(login_url="user:login")
def deTail(request,id):
    medicine= Recete.objects.filter(id=id).first()

    context={
        "medicine":medicine,
        
             }
        
    return render(request,"detail.html",context)
@login_required(login_url="user:login")
def send_mail(request,id):
    medicine= Recete.objects.filter(id=id).first()
    message= Recete.objects.filter(id=id)
    if request.method=="POST":
        mail= message.values_list('hasta__mail',flat=True).first()
        patient=message.values_list('hasta__first_name',flat=True).first()
        qr_code=message.values_list('qr_code',flat=True).first()
        total=message.values_list('toplam',flat=True).first()
        ilaclar=message.values_list("ilaclar",flat=True).first()
        
        #http://localhost:8000/media/ 
        #C:/Users/gundu/OneDrive/Masaüstü/smartPharmacy/uploads/   
        filename = "C:/Users/gundu/OneDrive/Masaüstü/smartPharmacy/uploads/" + qr_code
        image_name = Path(filename).name
        subject = "İlaçlarınızı eczane otomatından almayı unutmayınız."
        text_message = f"Email with a nice embedded image {image_name}."
        html_message = f"""
        <!doctype html>
        <html lang=en>
        <head>
            <meta charset=utf-8>
            <title>Some title.</title>
        </head>
        <body>
           <h2>{subject}</h2> 
            <p>
            <h3 style='color:red; font-family:verdana'>Toplam Tutar: {total} ₺</h3>
            <h3>İlaçlarınız: {ilaclar}</h3>
            <img src='cid:{image_name}'/>
            </p>
        </body>
        </html>
        """
        email=EmailMultiAlternatives(
            "Sayın"+ patient +", Reçeteniz ",
            subject,
            settings.EMAIL_HOST_USER,
            [mail],


        )
        if all([text_message,filename,image_name]):
            email.attach_alternative(html_message, "text/html")
            email.content_subtype = 'html'  
            with open(filename, mode='rb') as f:
                image = MIMEImage(f.read())
                email.attach(image)
                image.add_header('Content-ID', f"<{image_name}>")

        email.send()

        
        messages.success(request,"Mail başarıyla gönderildi")
    context={
        "medicine":medicine,
        
             }
        
    return render(request,"detail.html",context)