from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import EmployeeLogin
from django.contrib.auth.hashers import make_password, check_password

def add_employee_login(request):
    if request.method == 'POST':
        login_id = request.POST['login_id']
        password = request.POST['password']
        hashed_password = make_password(password) 

        new_employee = EmployeeLogin(login_id=login_id, password=hashed_password)
        new_employee.save()
        return HttpResponse('Employee login added successfully!')
    return render(request, 'add_employee_login.html')

def update_employee_login(request, user_id):
    try:
        employee = EmployeeLogin.objects.get(user_id=user_id)
    except EmployeeLogin.DoesNotExist:
        return HttpResponse('Employee not found')

    if request.method == 'POST':
        login_id = request.POST['login_id']
        password = request.POST['password']
        hashed_password = make_password(password)

        employee.login_id = login_id
        employee.password = hashed_password
        employee.save()

        return HttpResponse('Employee login updated successfully!')

    return render(request, 'update_employee_login.html', {'employee': employee})

def fetch_employee_login(request, user_id):
    try:
        employee = EmployeeLogin.objects.get(user_id=user_id)
        return render(request, 'view_employee_login.html', {'employee': employee})
    except EmployeeLogin.DoesNotExist:
        return HttpResponse('Employee not found')

def show_all_logins(request):
    employees = EmployeeLogin.objects.all()
    return render(request, 'show_all_logins.html', {'employees': employees})
