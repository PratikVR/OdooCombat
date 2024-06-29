from django.shortcuts import render, redirect
from grievance_app.models import * 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password

# Create your views here.
def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')

        if 'Emp' in user_name:
            employee_user = Employee_db.objects.filter(username = user_name)
        elif 'HR' in user_name:
            employee_user = HR_db.objects.filter(username = user_name)
        elif 'admin' in user_name:
            employee_user = Administrator_db.objects.filter(username = user_name)
            
        if employee_user:
            request.session['user_name'] = employee_user[0].username 
            if check_password(password, employee_user[0].password):
                return render(request, 'emp_home.html', {'user_data' : employee_user})
            else:
                return redirect('/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')



def emp_home(request):
    if request.method == 'POST':
        user_id = request.GET.get('user_name')
        print(user_id)
        # emp_email = request.POST.get('email')
        dept_name = request.POST.get('dept')
        event_date = request.POST.get('event_date')
        G_title = request.POST.get('title')
        descp = request.POST.get('Description')
        severity = request.POST.get('severity')

        
        new_request = grievance_db.objects.create(
            user_id = user_id,
            G_title = G_title,
            G_desc = descp,
            user_dept = dept_name,
            severity = severity,
            event_date = event_date,
            status = 0,
        )

        if request.Files['documents'] != 0:
            grievance_db.files = request.Files['documents']
        
        

    return render(request, 'emp_home.html')







def input_data(request):
    print('hello')
    if request.method == 'POST':
        print('world')
        email = request.POST.get('email')
        password = request.POST.get('password')
        emp_id = request.POST.get('emp_id')
        dept = request.POST.get('d_id')
        firstname = request.POST.get('firstname')
        phone = request.POST.get('phone')

        setted_password = set_password(password)

        user = Employee_db.objects.create(
            username = emp_id,
            firstname = firstname,
            emp_dept = dept,
            phone_no = phone,
            email = email,
            password = setted_password
        )

        user.save()
    return render(request, 'inputs.html')