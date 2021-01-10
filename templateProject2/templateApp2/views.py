from django.shortcuts import render
def EmployeeView(request):
    Ename=input("Enter the name")
    Edesignation=input("Enter the designation")
    Eexp=float(input("Enter the experience"))
    Esalary=int(input("Enter the salary"))
    d={'name':Ename,'desig':Edesignation,'exp':Eexp,'sal':Esalary}
    return render(request,'templateApp2/1.html',d)
# Create your views here.
