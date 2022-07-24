from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse, HttpResponse

from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as loginn
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile

from django.conf import settings
from coinbase_commerce.client import Client
from django.views.decorators.csrf import csrf_exempt
from coinbase_commerce.webhook import Webhook
from django.views.decorators.http import require_http_methods
from coinbase_commerce.error import SignatureVerificationError, WebhookInvalidPayload
import logging
from django.http import HttpResponse
import time
from .forms import signup
from json import dumps

import stripe
stripe.api_key = settings.STRIPE_PRIVATE_KEY



# # Create your views here.
def home(request):

    if request.method == 'POST':
        form=signup(request.POST)
        form2 =AuthenticationForm(data=request.POST)
        # username=request.user.username
        # new=payment.objects.create(user='test' ,amount=2)
        # new.save()
        if form2.is_valid():
            user=form2.get_user()
            loginn(request, user)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
            loginn(request, new_user)

    else:
        form2=AuthenticationForm()
    form = signup()

    return render(request,'index.html',{"form":form,'form2':form2})








def photographer(request):

    if request.method == 'POST':
        form=signup(request.POST)
        form2 =AuthenticationForm(data=request.POST)
        # username=request.user.username
        # new=payment.objects.create(user='test' ,amount=2)
        # new.save()
        if form2.is_valid():
            user=form2.get_user()
            loginn(request, user)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
            loginn(request, new_user)

    else:
        form2=AuthenticationForm()
    form = signup()

    return render(request,'phtographer.html',{"form":form,'form2':form2})
def designer(request):

    if request.method == 'POST':
        form=signup(request.POST)
        form2 =AuthenticationForm(data=request.POST)
        # username=request.user.username
        # new=payment.objects.create(user='test' ,amount=2)
        # new.save()
        if form2.is_valid():
            user=form2.get_user()
            loginn(request, user)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
            loginn(request, new_user)

    else:
        form2=AuthenticationForm()
    form = signup()

    return render(request,'designer.html',{"form":form,'form2':form2})
def artist(request):

    if request.method == 'POST':
        form=signup(request.POST)
        form2 =AuthenticationForm(data=request.POST)
        # username=request.user.username
        # new=payment.objects.create(user='test' ,amount=2)
        # new.save()
        if form2.is_valid():
            user=form2.get_user()
            loginn(request, user)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
            loginn(request, new_user)

    else:
        form2=AuthenticationForm()
    form = signup()

    return render(request,'artist.html',{"form":form,'form2':form2})
def illustrator(request):

    if request.method == 'POST':
        form=signup(request.POST)
        form2 =AuthenticationForm(data=request.POST)
        # username=request.user.username
        # new=payment.objects.create(user='test' ,amount=2)
        # new.save()
        if form2.is_valid():
            user=form2.get_user()
            loginn(request, user)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
            loginn(request, new_user)

    else:
        form2=AuthenticationForm()
    form = signup()

    return render(request,'illustrator.html',{"form":form,'form2':form2})
def makeup(request):

    if request.method == 'POST':
        form=signup(request.POST)
        form2 =AuthenticationForm(data=request.POST)
        # username=request.user.username
        # new=payment.objects.create(user='test' ,amount=2)
        # new.save()
        if form2.is_valid():
            user=form2.get_user()
            loginn(request, user)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
            loginn(request, new_user)

    else:
        form2=AuthenticationForm()
    form = signup()

    return render(request,'makeup.html',{"form":form,'form2':form2})




def edit(request):
    if request.method == 'POST':
        html= request.POST.get('html', False)
        css= request.POST.get('css', False)
        domain= request.POST.get('domain', False)
        name= request.POST.get('name', False)
        form=signup(request.POST)
        form2 =AuthenticationForm(data=request.POST)
        username=request.user
        if form2.is_valid():
            user=form2.get_user()
            loginn(request, user)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
            loginn(request, new_user)
        Profile.objects.filter(user = username).update(html = html,css=css,domain_name=domain,website_name=name)

    else:
        form2=AuthenticationForm()
    form = signup()
    return render(request,'grapes/index.html',{"form":form,'form2':form2})



















def category(request):
    if request.method == 'POST':
        form=signup(request.POST)
        form2 =AuthenticationForm(data=request.POST)
        # username=request.user.username
        # new=payment.objects.create(user='test' ,amount=2)
        # new.save()
        if form2.is_valid():
            user=form2.get_user()
            loginn(request, user)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
            loginn(request, new_user)
    else:
        form2=AuthenticationForm()
    form = signup()

    return render(request,'category.html',{"form":form,'form2':form2})


@login_required()
def user(request):
    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
    domain_url = 'http://localhost:8000/'
    product = {
        'name': 'Coffee',
        'description': 'A really good local coffee.',
        'local_price': {
            'amount': '0.01',
            'currency': 'USD'
        },
        'pricing_type': 'fixed_price',
        'redirect_url': domain_url + 'success/',
        'cancel_url': domain_url + 'cancel/',
        'metadata': {
            'customer_id': request.user.id if request.user.is_authenticated else None,
            'customer_username': request.user.username if request.user.is_authenticated else None,
        },
    }
    charge = client.charge.create(**product)

    return render(request,'user.html',{'charge': charge,})



@csrf_exempt
def checkout(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1LOnfCFnAE8OxnmaKRo8i7nU',
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('thanks')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('landing')),
    )

    return JsonResponse({
        'session_id' : session.id,
        'stripe_public_key' : settings.STRIPE_PUBLIC_KEY
    })

@csrf_exempt
def checkout2(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1LOngvFnAE8OxnmaJCpYNkQl',
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('thanks2')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('landing')),
    )

    return JsonResponse({
        'session_id' : session.id,
        'stripe_public_key' : settings.STRIPE_PUBLIC_KEY
    })

@csrf_exempt
def checkout3(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1LOnhfFnAE8OxnmaMco4HD5C',
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('thanks3')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('landing')),
    )

    return JsonResponse({
        'session_id' : session.id,
        'stripe_public_key' : settings.STRIPE_PUBLIC_KEY
    })



def logout_user(request):
    logout(request)
    return redirect('landing')

def success_view(request):
    return redirect('landing')


def cancel_view(request):
    return redirect('landing')


def thanks(request):
    username=request.user
    Profile.objects.filter(user = username).update(plan="basic")
    return render(request, 'thanks.html')


def thanks2(request):
    username=request.user
    Profile.objects.filter(user = username).update(plan="pro")
    return render(request, 'thanks.html')


def thanks3(request):
    username=request.user
    Profile.objects.filter(user = username).update(plan="business")
    return render(request, 'thanks.html')





# @csrf_exempt
# @require_http_methods(['POST'])
# def coinbase_webhook(request):
#     logger = logging.getLogger(__name__)

#     request_data = request.body.decode('utf-8')
#     request_sig = request.headers.get('X-CC-Webhook-Signature', None)
#     webhook_secret = settings.COINBASE_COMMERCE_WEBHOOK_SHARED_SECRET

#     try:
#         event = Webhook.construct_event(request_data, request_sig, webhook_secret)

#         # List of all Coinbase webhook events:
#         # https://commerce.coinbase.com/docs/api/#webhooks

#         if event['type'] == 'charge:confirmed':
#             logger.info('Payment confirmed.')
#             customer_id = event['data']['metadata']['customer_id']
#             customer_username = event['data']['metadata']['customer_username']
#             # TODO: run some custom code here
#             # you can also use 'customer_id' or 'customer_username'
#             # to fetch an actual Django user

#     except (SignatureVerificationError, WebhookInvalidPayload) as e:
#         return HttpResponse(e, status=400)

#     logger.info(f'Received event: id={event.id}, type={event.type}')
#     return HttpResponse('ok', status=200)




@csrf_exempt
def stripe_webhook(request):

    print('WEBHOOK!')
    # You can find your endpoint's secret in your webhook settings
    endpoint_secret = 'whsec_b00ecef1a5b38842b98292ee2723e5e935156af9cff4b1ae8cecdf993e1b61d9'

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(event['data'])
        Profile.objects.filter(user = "superuser").update(plan="business")


    return HttpResponse(status=200)