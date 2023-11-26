from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, AccountRequestForm
from .models import User, UserLoggedIn, AccountRequestTable

# Create your views here.
def registration(request):
    fm = RegistrationForm()

    if request.method == 'POST':
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            name = fm['name'].value()
            email = fm['email'].value()
            password = fm['password'].value()

            # Validation Needed
            # -----------------

            # Saving the data
            count = User.objects.all().count()
            user_id = f'U{count+1}'
            instance = User(user_id=user_id, name=name, email=email, password=password)
            instance.save()
            msg = 'Your account is created successfully'
            return redirect('login', msg)

    return render(request, 'user/register_page.html', {'form':fm})


def login(request, msg=''):
    fm = LoginForm()
    if request.method == 'GET':
        msg = msg

    elif request.method == 'POST':
        fm = LoginForm(request.POST)
        given_email = request.POST['email']
        given_password = request.POST['password']
        
        # Vairfication
        registered = User.objects.filter(email=given_email).exists()
        if registered:
            msg = ''

            users = User.objects.filter(email=given_email)
            for user in users:
                user_password = user.password
                user = user
            
            if user_password == given_password:
                if not UserLoggedIn.objects.filter(logged_id=user).exists():
                    instance = UserLoggedIn(logged_id=user)
                    instance.save()
                return redirect('homepage', id=user.user_id)
            else:
                msg = 'Incorrect password'
            
            return render(request, 'user/login_page.html', {'form':fm, 'error_msg':msg})

    return render(request, 'user/login_page.html', {'form':fm, 'msg':msg})

def logout(request, id):
    msg = ''
    if request.method == 'GET':
        instance = UserLoggedIn.objects.filter(logged_id=id)
        print(instance)
        instance.delete()
        msg = "You are logged out"
    return redirect('login', msg=msg)


def requestAccount(reqeust, msg=''):
    fm = AccountRequestForm()
    if reqeust.method == 'POST':
        fm = AccountRequestForm(reqeust.POST)
        if fm.is_valid():
            name = fm['name'].value()
            email = fm['email'].value()
            description = fm['description'].value()
            instance = AccountRequestTable(name=name, email=email, description=description)
            instance.save()
            msg = "Your request has been sent"

    return render(reqeust, 'user/request_account_page.html', {'form':fm, 'msg':msg})