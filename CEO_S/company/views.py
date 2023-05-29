from django.shortcuts import render, redirect
from .models import Ceo, Company
from .forms import CompanyForm, InfoForm


# Create your views here.
def ceo_view(request):
    form = InfoForm
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company')
    template_name = 'company/ceo.html'
    context = {'form' : form}
    return render(request ,template_name, context)

def company_view(request):
    form = CompanyForm
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'company/company.html'
    context = {'form' : form}
    return render(request ,template_name, context)

def company_show_view(request):
    data = Company.objects.all()
    dat = Ceo.objects.all()
    context = {'data' : data, 'dat' : dat}
    template_name = 'company/show.html'
    return render(request, template_name, context)    
    

def info_update_view(request, pk):
    data = Ceo.objects.get(id=pk)
    form = InfoForm(instance=data)
    if request.method == 'POST':
        form = InfoForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
        return redirect('show')
    template_name = 'company/ceo.html'
    context = {'form' : form}
    return render(request, template_name, context)

def company_update_view(request, pk):
    data = Company.objects.get(id=pk)
    form = CompanyForm(instance=data)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
        return redirect('show')
    template_name = 'company/company.html'
    context = {'form' : form}
    return render(request, template_name, context)

def delete_ceo_view(request, pk):
    data = Ceo.objects.get(id=pk)
    if request.method == "POST":
        data.delete()
        return redirect('show')
    template_name = 'company/delete.html'
    context = {'data':data}
    return render(request,template_name ,context)

def delete_company_view(request, pk):
    dat = Company.objects.get(id=pk)
    if request.method == "POST":
        dat.delete()
        return redirect('show')
    template_name = 'company/delete.html'
    context = {'data':dat}
    return render(request,template_name ,context)