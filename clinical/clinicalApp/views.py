from aiohttp import request
from django.shortcuts import render

# Create your views here.
from clinicalApp.models import Patient,ClinicData
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from clinicalApp.froms import clinicaldataForm
from django.shortcuts import redirect
\

class Patientlistview(ListView):
    model=Patient

class Patientcreateview(CreateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstname','lastname','age')

class Patientupdateview(UpdateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstname','lastname','age')

class Patientdeleteview(DeleteView):
    model=Patient
    success_url=reverse_lazy('index')

def datadd(request,**kwargs):
    form = clinicaldataForm()
    pateint =Patient.objects.get(id=kwargs['pk'])
    if request.method =='POST':
        form=clinicaldataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'clinicalApp/clinicaldata_form.html',{'form':form,'patient':pateint})
    
    
def analyse(request,**kwargs):
    data=ClinicData.objects.filter(patient_id=kwargs['pk'])
    responsedata=[]
    for i in data:
        if i.componentname =="hw":
               higetandweight=i.componentval.split('/')
               if len(higetandweight)>1:
                   feettometer=float(higetandweight[0])*0.4536
                   bmi=float(higetandweight[1])/(feettometer**feettometer)
                   bmientry= ClinicData
                   bmientry.componentname='BMI'
                   bmientry.componentval='BMI'
                   responsedata.append(bmientry)
        responsedata.append(i)

    return render(request,'clinicalApp/generate.html',{'data':responsedata})

