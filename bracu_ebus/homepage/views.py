from django.shortcuts import render, redirect
from user.models import User, UserLoggedIn

# Create your views here.
def homePage(request, id=None, user_type=None):
    if request.method == "GET":
        if id == None and user_type == None:
            msg = "You are not logged in!"
            return redirect('login', msg)
        else:
            if user_type == 'User':
                if UserLoggedIn.objects.filter(logged_id=id).exists():
                    user = User.objects.filter(user_id=id).first()
                    # Write here if needed


                    return render(request, 'homepage/home_page.html', {'user_type':'User', 'user':user})
                else:
                    msg = "You are not logged in!"
                    return redirect('login', msg)