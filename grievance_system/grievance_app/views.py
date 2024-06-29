from django.shortcuts import render, redirect
from grievance_app.models import * 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail

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
                send_mail(
                    "New Grievance Posted!",

                    f"""Your Employee {employee_user[0].firstname} 
                    post a grievance message.""",

                    "Your_email_id",
                    [employee_user[0].email],
                    fail_silently = False,
                )
                return render(request, 'emp_home.html', {'user_data' : employee_user[0]})
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')



def emp_home(request):
    if request.method == 'POST':
        user_id = request.session.get('user_name')
        event_date = request.POST.get('event_date')
        G_title = request.POST.get('title')
        descp = request.POST.get('Description')
        severity = request.POST.get('severity')

        new_request = grievance_db.objects.create(
            user_id = user_id,
            G_title = G_title,
            G_desc = descp,
            severity = severity,
            event_date = event_date,
            status = '0'
        )
        
        if len(request.FILES) != 0:
            new_request.files = request.FILES['documents']
        
        if 'Emp' in user_id:
            employee_user = Employee_db.objects.filter(username = user_id)
        elif 'HR' in user_id:
            employee_user = HR_db.objects.filter(username = user_id)
        elif 'admin' in user_id:
            employee_user = Administrator_db.objects.filter(username = user_id)

        new_request.user_dept = employee_user[0].emp_dept
        new_request.save()

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