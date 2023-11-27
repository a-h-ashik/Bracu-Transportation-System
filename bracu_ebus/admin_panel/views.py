from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CreateStaffForm, AdminLoginForm, RouteCreationForm
from .models import Staff, Admin, AdminLoggedIn
from user.models import User, AccountRequestTable
from user.forms import RegistrationForm

from ticket_booking.models import Buses

# Additional functions


# Create your views here.
def adminLogin(request):
    msg = ''
    error_msg = ''
    fm = AdminLoginForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        given_passwod = request.POST.get('password')
        if Admin.objects.filter(name=name).exists():
            admins = Admin.objects.filter(name=name)
            for admin in admins:
                admin = admin
                password = admin.password

            if password == given_passwod:
                if not AdminLoggedIn.objects.filter(logged_id=admin).exists():
                        instance = AdminLoggedIn(logged_id=admin)
                        instance.save()
                print(admin.admin_id)
                return redirect('admin')
            else:
                error_msg = 'Incorrect password'
        else:
            error_msg = 'Incorrect username'


    return render(request, 'admin_panel/admin_login_page.html', {'form':fm, 'msg':msg, 'error_msg':error_msg})

def adminLogout(request):
    instance = AdminLoggedIn.objects.all().first()
    instance.delete()
    return redirect('admin_login')

def adminPage(request):
    if AdminLoggedIn.objects.all().count() > 0:
        return render(request, 'admin_panel/admin_page.html')
    return redirect('admin_login')
    
def userTable(request):
    users = User.objects.all()
    fm = RegistrationForm()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        if not User.objects.filter(email=email).exists():
            count = User.objects.all().count()
            user_id = f'U{count+1}'
            instance = User(user_id=user_id, name=name, email=email, password='0000')
            instance.save()
    return render(request, 'admin_panel/all_users.html', {'users': users, 'form':fm})

def staffTable(request):
    if request.method == "POST":
        data = request.POST
        fm = CreateStaffForm(data)

        name = fm['name'].value()
        email = fm['email'].value()
        if fm.is_valid():
            total_staff = Staff.objects.all().count()
            staff_id = f'S{total_staff+1}'
            instance = Staff(staff_id=staff_id, name=name, email=email)
            instance.save()
    staffs = Staff.objects.all()
    fm = CreateStaffForm()
    return render(request, 'admin_panel/all_staffs.html', {'staffs': staffs, 'form':fm})

def deleteUser(request, id):
    instance = User.objects.filter(user_id=id)
    instance.delete()
    return redirect('all_users')

def accountRequestTable(request):
    acc_requests = AccountRequestTable.objects.all()
    return render(request, 'admin_panel/account_request_page.html', {'acc_requests':acc_requests})


def deleteAccountRequest(request, email):
    instance = AccountRequestTable.objects.filter(email=email)
    instance.delete()
    return redirect('all_account_requests')


def busTable(request):
    buses = Buses.objects.all()
    fm = RouteCreationForm()

    if request.method == 'POST':
        instance = Buses(bus_number=request.POST.get('bus_number'),
                         d1=request.POST.get('d1'),
                         d2=request.POST.get('d2'),
                         d3=request.POST.get('d3'),
                         d4=request.POST.get('d4'),
                         d5=request.POST.get('d5'),
                         active=True)

        instance.save()
        return redirect('all_routes')
    return render(request, 'admin_panel/routes.html', {'buses':buses, 'form':fm})