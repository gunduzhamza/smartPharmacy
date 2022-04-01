from django.shortcuts import render,redirect
from matplotlib.style import context
from sympy import content
from medicine.forms import *
from django.contrib import messages
from medicine.models import Medicine, Patient

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

        messages.success(request,"Hasta başarıyla oluşturuldu")
        return redirect("index")

    return render(request,"addpatient.html",{"form":form})

def receteolustur(request):
    form=ReceteForm()
    if request.method=="POST":
        form=ReceteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Reçete başarıyla oluşturuldu")
            return redirect("/")

    context={"form":form}
    return render(request,"receteolustur.html",context)

def ilacListesi(request):
    ilaclar=Medicine.objects.all()
    context={
        "ilaclar":ilaclar
    }
    return render(request,"ilaclistesi.html",context)