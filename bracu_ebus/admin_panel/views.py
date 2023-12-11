from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CreateStaffForm, AdminLoginForm, RouteCreationForm
from .models import Staff, Admin, AdminLoggedIn
from user.models import User, AccountRequestTable
from user.forms import RegistrationForm

from ticket_booking.models import Buses

#My
from ticket_booking.models import Tickets
from django.db.models import Count
from django.db.models.functions import Cast
from django.db.models.fields import DateField
from django.utils import timezone
from django.contrib import messages
from datetime import datetime, timedelta

# Create your views here.
def adminLogin(request):
    msg = ''
    error_msg = ''
    fm = AdminLoginForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        given_password = request.POST.get('password')
        if Admin.objects.filter(name=name).exists():
            admins = Admin.objects.filter(name=name)
            for admin in admins:
                admin = admin
                password = admin.password

            if password == given_password:
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

#my
def adminPage(request):
    if AdminLoggedIn.objects.all().count() > 0:
        # total number of booked tickets-my
        total_tickets = Tickets.objects.all().count()
        total_available_buses = Buses.objects.filter(active=True).count()

        # user with the maximum number of tickets-my
        max_ticket_buyer = Tickets.objects.values('user_id').annotate(total_tickets=Count('user_id')).order_by('-total_tickets').first()
        # user details corresponding to the user_id
        user_details = User.objects.filter(user_id=max_ticket_buyer['user_id']).first()

        # total number of users-my
        total_users = User.objects.all().count()

         # total number of staff members-my
        total_staff_members = Staff.objects.all().count()

        # total number of users based on the join date field-my
        users_date_joined = (
            User.objects
            .annotate(joined_day=Cast('date_joined', DateField()))
            .values('joined_day')
            .annotate(count=Count('user_id'))
            .order_by('joined_day')
        )

        # total number of users weekly-my
        total_users_count = sum(entry['count'] for entry in users_date_joined)
    
        return render(request, 'admin_panel/admin_page.html', {'total_tickets': total_tickets, 'total_available_buses': total_available_buses, 'max_ticket_buyer': max_ticket_buyer, 'user_details': user_details, 'total_users': total_users, 'total_staff_members': total_staff_members, 'users_date_joined': users_date_joined, 'total_users_count': total_users_count})
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

#my
def staffTable(request):
    staffs = Staff.objects.all()
    fm = CreateStaffForm()

    if request.method == "POST":
        fm = CreateStaffForm(request.POST)  # Pass POST data to the form
        name = request.POST.get('name')
        email = request.POST.get('email')

        if fm.is_valid():
            total_staff = Staff.objects.all().count()
            staff_id = f'S{total_staff+1}'
            instance = Staff(staff_id=staff_id, name=name, email=email, password='0000')
            instance.save()
    return render(request, 'admin_panel/all_staffs.html', {'staffs': staffs, 'form':fm})

def deleteUser(request, id):
    instance = User.objects.filter(user_id=id)
    instance.delete()
    return redirect('all_users')

#my
def deleteStaff(request, id):
    instance = Staff.objects.filter(staff_id=id)
    instance.delete()
    return redirect('all_staffs')

def deleteBus(request, id):
    instance = Buses.objects.filter(bus_number=id)
    instance.delete()
    return redirect('all_routes')

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


#my
def admin_add_points(request, user_id):
    user = User.objects.filter(user_id=user_id).first()

    if user:
        # Check if a week has passed since the last bonus
        last_bonus_timestamp = request.session.get('bonus_timestamp')
        if last_bonus_timestamp:
            last_bonus_timestamp = datetime.fromisoformat(last_bonus_timestamp)
            one_week_ago = timezone.now() - timedelta(weeks=1)
            if last_bonus_timestamp > one_week_ago: #change < to get congratulation
                messages.warning(request, 'You can only receive a bonus once a week.')
                return redirect('admin')
            

        # Add 50 points to the user
        user.point += 50
        user.save()

        # to indicate that the bonus has been added
        request.session['bonus_added'] = True

        # to store the timestamp when the bonus was added as a string
        request.session['bonus_timestamp'] = str(timezone.now())

        # Send congratulatory notification
        messages.success(request, 'Congratulation! You received a bonus of 50 points.')

        return redirect('admin')
    
