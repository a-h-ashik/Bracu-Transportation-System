from django.shortcuts import render, redirect
from user.models import User, UserLoggedIn
from ticket_booking.models import Tickets, Buses

from homepage.forms import Lostitem
from homepage.models import Lost

from stuff_panel.models import OfferTable


# Create your views here.
def homePage(request, id=None):
    if request.method == "GET":
        if id == None:
            msg = "You are not logged in!"
            return redirect('login', msg)
        else:
            offers = OfferTable.objects.all()
            if UserLoggedIn.objects.filter(logged_id=id).exists():
                user = User.objects.filter(user_id=id).first()
                # Write here if needed
                buses = Buses.objects.all()

                return render(request, 'homepage/home_page.html', {'user':user, 'user_id':user.user_id, 'buses':buses,'offers':offers})
            else:
                msg = "You are not logged in!"
                return redirect('login', msg)

def ticketPage(request, id):
    user = User.objects.filter(user_id=id).first()
    ticket = Tickets.objects.filter(user_id=id).last()
    return render(request, 'homepage/show_ticket.html', {'user':user, 'ticket': ticket})


def cancelTicket(requst, id, ticket_id):
    user = User.objects.filter(user_id=id).first()
    user.point = user.point + 50
    user.save()


    instance = Tickets.objects.filter(ticket_id=ticket_id).last()
    instance.delete()


    return redirect('homepage', id=user.user_id)



def itemshow(request, id):
    user = User.objects.filter(user_id=id).first()
    if request.method == 'POST':
        fm= Lostitem(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        lostitem = request.POST['lostitem']
        description = request.POST['description']
        reg=Lost(name=name, email=email,lostitem=lostitem,description=description)
        reg.save()
        fm= Lostitem()
        
    else:
        fm= Lostitem()
    #alldata=Lost.objects.all()
    return render(request, 'homepage/lostitem.html',{'user':user,'form' : fm})



def showpoints(request,id):
    user = User.objects.filter(user_id=id).first()
    fetchdata=User.objects.all()
    print(fetchdata)
    return render(request, 'homepage/showpoints.html',{'user':user,'fetchdata':fetchdata})


def complainshow(request):
    lvalue=Lost.objects.all()
    return render(request,'homepage/showcomplain.html',{'complain':lvalue})

