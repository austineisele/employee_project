from django.shortcuts import redirect, render
from django.template import context
from employee_register.forms import EmployeeForm
from .models import Employee

# Create your views here.

#this will be to view the data
def employee_list(request):
    #we need to give it the context for the data
    context = {'employee_list': Employee.objects.all()}
    #we then pass the context to the render method
    return render(request, "employee_register/employee_list.html", context)

#this will be insert and update - the option parameter of 0 for inserting new records
def employee_form(request, id=0):
    #determine if this is a get or post request
    if request.method == "GET":
        #deteremine if it's an insert or update operation
        if id==0:
            #this instantiates the employee form
            form = EmployeeForm()
        else:
            #next we get the employee using the id with the get method
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
       #now you'll need to pass this from to the render request. The syntax is with the {} 
        return render(request, "employee_register/employee_form.html", {'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee) 
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


#this will be to delete data
def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete() 
    return redirect('/employee/list')
  
