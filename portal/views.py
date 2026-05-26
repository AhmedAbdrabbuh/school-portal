from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Payment
from decimal import Decimal, InvalidOperation

# Create your views here.

def home(request):
    return render(request, 'portal/home.html')

@login_required
def payment_portal(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        description = request.POST.get('description')

        if amount and description:
            try:
                Payment.objects.create(
                    user=request.user,
                    amount=Decimal(amount),
                    description=description
                )
                messages.success(request, 'Payment submitted successfully!')
                return redirect('payment')
            except InvalidOperation:
                messages.error(request, 'Invalid amount.')
        else:
            messages.error(request, 'Please provide both amount and description.')

    payments = Payment.objects.filter(user=request.user).order_by('-date')
    return render(request, 'portal/payment.html', {'payments': payments})
