from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from emp.forms import EmployeeForm,latestnewsform,calendarform,jobform
from emp.models import Employee,Latestnews,Calendar,JobOpening
import csv
from django.views.generic import ListView, DetailView,UpdateView, DeleteView


# Create your views here.

def base(request):
    return render(request,'emp/base.html')

def home(request):
    return render(request,'emp/home.html')

@login_required
def hr(request):
    return render(request,'emp/hr.html')

def employee(request):
    return render(request,'emp/employee.html')

def addemployee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewemployee')
    return render(request, 'emp/addemployee.html', {'form': form})

def viewemployee(request):
    employees = Employee.objects.all()
    return render(request, 'emp/viewemployee.html', {'employees': employees})

def updateview(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('viewemployee')
    return render(request, 'emp/update.html', {'form': form})

def delete(request,pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return redirect('viewemployee')

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'

    writer = csv.writer(response)
    writer.writerow(['Emp_Name', 'Emp_ID', 'Designation', 'Date_of_joining', 'Department', 'Annual_CTC', 'Experience'])

    employees = Employee.objects.all().values_list('Emp_Name', 'Emp_ID', 'Designation', 'Date_of_joining', 'Department', 'Annual_CTC', 'Experience')
    for employee in employees:
        writer.writerow(employee)

    return response

def addnews(request):
    form = latestnewsform()
    if request.method == 'POST':
        form = latestnewsform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')  # ← save hone ke baad news page
    return render(request, 'emp/addnews.html', {'form': form})

def latestnews(request):
    news = Latestnews.objects.all()
    return render(request, 'emp/latestnews.html', {'news': news})

def newsdetail(request, pk):
    data = Latestnews.objects.get(id=pk)
    return render(request, 'emp/detail.html', {'data': data})


class NewsUpdateView(UpdateView):
    model = Latestnews
    form_class = latestnewsform
    template_name = 'emp/addnews.html'
    success_url = reverse_lazy('news')

  
class NewsDeleteView(DeleteView):
    model = Latestnews
    success_url = reverse_lazy('news')

def calendar(request):
    form = calendarform()
    if request.method == 'POST':
        form = calendarform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('holidays')  
    return render(request, 'emp/calendar.html', {'form': form})

    
def holidays(request):
    calendar = Calendar.objects.all()
    
    return render(request, 'emp/holidays.html', {'calendar': calendar})


def jobopen(request):
    form = jobform()
    if request.method == 'POST':
        form = jobform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobdata')
    return render(request, 'emp/job.html', {'form': form})

def viewjob(request):
    jobs = JobOpening.objects.all()
    
    return render(request, 'emp/jobdata.html', {'jobs': jobs})

