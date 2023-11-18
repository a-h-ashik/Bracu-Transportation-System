from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CreateStaffForm, AdminLoginForm
from .models import Staff, Admin, AdminLoggedIn
from user.models import User

# Additional functions


# Create your views here.
def adminLogin(request):
    msg = ''
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
                return redirect('admin')
            else:
                error_msg = 'Incorrect password'
        else:
            error_msg = 'Incorrect username'


    return render(request, 'admin_panel/admin_login_page.html', {'form':fm, 'msg':msg, 'error_msg':error_msg})


def adminPage(request):
    return render(request, 'admin_panel/admin_page.html')

def userTable(request):
    users = User.objects.all()

    return render(request, 'admin_panel/all_users.html', {'users': users})

def staffTable(request):
    if request.method == "POST":
        data = request.POST
        fm = CreateStaffForm(data)

        name = fm['name'].value()
        email = fm['email'].value()
        if fm.is_valid():
            total_staff = Staff.objects.all().count()
            staff_id = f'#{total_staff+1}'
            instance = Staff(staff_id=staff_id, name=name, email=email)
            instance.save()
    staffs = Staff.objects.all()
    fm = CreateStaffForm()
    return render(request, 'admin_panel/all_staffs.html', {'staffs': staffs, 'form':fm})
