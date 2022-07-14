from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
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




def logout_user(request):
    logout(request)
    return redirect('landing')

def success_view(request):
    return redirect('landing')


def cancel_view(request):
    return redirect('landing')

@csrf_exempt
@require_http_methods(['POST'])
def coinbase_webhook(request):
    logger = logging.getLogger(__name__)

    request_data = request.body.decode('utf-8')
    request_sig = request.headers.get('X-CC-Webhook-Signature', None)
    webhook_secret = settings.COINBASE_COMMERCE_WEBHOOK_SHARED_SECRET

    try:
        event = Webhook.construct_event(request_data, request_sig, webhook_secret)

        # List of all Coinbase webhook events:
        # https://commerce.coinbase.com/docs/api/#webhooks

        if event['type'] == 'charge:confirmed':
            logger.info('Payment confirmed.')
            customer_id = event['data']['metadata']['customer_id']
            customer_username = event['data']['metadata']['customer_username']
            # TODO: run some custom code here
            # you can also use 'customer_id' or 'customer_username'
            # to fetch an actual Django user

    except (SignatureVerificationError, WebhookInvalidPayload) as e:
        return HttpResponse(e, status=400)

    logger.info(f'Received event: id={event.id}, type={event.type}')
    return HttpResponse('ok', status=200)

