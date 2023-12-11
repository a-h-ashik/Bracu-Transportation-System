from django.shortcuts import render, reverse
from django.conf import settings
from .models import paymentTable
from user.models import User
import stripe

from django.http import HttpResponse
from reportlab.pdfgen import canvas


stripe.api_key = settings.STRIPE_SECRET_KEY


def payment(request):
    publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, 'payment/payment.html', {'key': publishable_key})

def charge(request):
    if request.method == 'POST':
        try:
            # payment_method_data

            payment_intent = stripe.PaymentIntent.create(
                amount=500,
                currency='usd',
                description="A Django Charge",
                payment_method_data={
                    'type': 'card',
                    'card': {
                        'token': request.POST['stripeToken'],
                    },
                },
                confirm=True,
                return_url=request.build_absolute_uri(reverse('charge'))
            )
            # Extract payment information
            amount_paid = payment_intent.amount_received / 100
            payment_status = payment_intent.status
            token_number = request.POST['stripeToken']

            # Save payment information to paymentTable
            name = request.POST.get('name')
            email = request.POST.get('email')

            paymentTable.objects.create(
                name=name,
                email=email,
                amount=amount_paid,
                token_number=token_number,
                payment_status=payment_status,
                )
            
            # Retrieve the user
            user = User.objects.filter(name=name, email=email).first()

            if user:
                # Update the user's points by adding 100
                user.point += 100
                user.save()

            return render(request, 'payment/charge.html', {'name':name,'email':email, 'amount_paid': amount_paid, 'token_number': token_number, 'payment_status': payment_status})
        except stripe.error.CardError as e:
            # Handle CardError
            return render(request, 'payment/error.html', {'error': e.error.message})
        except stripe.error.StripeError as e:
            # Handle Stripe error
            return render(request, 'payment/error.html', {'error': e.error.message})


def generate_pdf(request):
    # latest successful payment data
    latest_payment = paymentTable.objects.filter(payment_status='requires_action').latest('payment_date')

    # Generate PDF content
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="payment_receipt.pdf"'

    # Create PDF document
    p = canvas.Canvas(response)
    p.drawString(100, 800, 'Payment Receipt')
    p.drawString(100, 780, '----------------------')

    # Add table content
    row_height = 20
    y_position = 750
    for field in latest_payment._meta.fields:
        field_name = field.name
        field_value = getattr(latest_payment, field_name)
        p.drawString(100, y_position, f'{field_name.capitalize()}: {field_value}')
        y_position -= row_height

    p.save()
    return response
