from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
from django.shortcuts import redirect
from .models import Employee

# def Home(request):
#     return HttpResponse("Hello world")

# Create view.
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm() 
    return render(request, 'create.html', {'form':form})

# list view
def employee_list(request):
    employee = Employee.objects.all()
    return render(request, 'list.html', {'employees':employee})

# update view
def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('list')
        
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update.html', {'form':form})

# delete view

def delete_employee(request, pk):
    employee = Employee.objects.get(id= pk)
    if request.method == "POST":
        employee.delete()
        return redirect('list')

# Create your views here.
