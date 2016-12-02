from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from store.models import Product, UserProfile, Transaction
from store.forms import addproductform, addbalanceform, moneyrequestform
from django.core.mail import send_mail
import datetime

# Create your views here.

def index(request):

    return render(request, 'store/index.html', {})

@login_required
def productlist(request):

	product_list = Product.objects.exclude(product_seller=request.user).filter(product_active=True)

   	context = {'products' : product_list}
	return render(request, 'store/homepage.html', context)

@login_required
def productdetails(request, pk):

	product = get_object_or_404(Product, pk=pk)

	context =  {'product' : product}

	return render(request, 'store/productdetails.html', context)

@login_required
def addproduct(request):

    if request.method == "POST":

        prodcutform = addproductform(request.POST, request.FILES)

        if prodcutform.is_valid():
            product = prodcutform.save(commit=False)
            product.product_seller = request.user
            product.product_image = prodcutform.cleaned_data["product_image"]
            product.save()
            return productlist(request)

    else:

        prodcutform = addproductform()

    return render(request, 'store/addproduct.html', {'form': prodcutform} )

@login_required
def sellinglist(request):

    product_list = Product.objects.filter(product_seller=request.user).filter(product_active=True)

    context = {'products' : product_list}
    return render(request, 'store/productsellinglist.html', context)

@login_required
def boughtlist(request):

    bought_list = Product.objects.filter(product_active=False).filter(product_beyer=request.user)

    context = {'products' : bought_list}
    return render(request, 'store/boughtlist.html', context)


@login_required
def productremove(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('sellinglist')

@login_required
def checkbalance(request):

    product_list = User.objects.get(username=request.user)
    context = {'products' : product_list.userprofile.balance}
    return render(request, 'store/profile.html', context)


@login_required
def buyproduct(request, pk):

    product = get_object_or_404(Product, pk=pk)
    user = User.objects.get(username=request.user)

    productcost = product.product_cost

    usrbalance = user.userprofile.balance

    if(usrbalance >= productcost):
        product.product_beyer = user.username
        product.product_active = False
        user.userprofile.balance = usrbalance - productcost
        product.save()
        user.save()
        transaction = Transaction.objects.create(transaction_seller=product.product_seller,
                                                     transaction_beyer=user.username,
                                                     transaction_product=product.product_name,
                                                        transaction_amount=product.product_cost,
                                                        transaction_date=datetime.datetime.now(),
                                                        transaction_time=datetime.datetime.now().time())


        return redirect('boughtlist')

    else:

        warning = "You do not have enough money to buy this product."
        context = {'product' : product, 'warning': warning}

        return render(request, 'store/test.html', context )


@login_required
def moneyrequest(request):

    if request.method == "POST":

        form = moneyrequestform(request.POST)

        if form.is_valid():
            money_request = form.save(commit=False)
            money_request.money_requester = request.user
            money_request.money_requester_email = request.user.email
            money_request.save()

            email_subject = 'Money Request for: ' + str(request.user)
            email_body ='Please approve my money request'

            send_mail(
                email_subject,
                email_body,
                'goatstore92@gmail.com',
                ['goatstore92@gmail.com'],
                fail_silently=True,
            )


            return redirect('home')
    else:

        form = moneyrequestform()

    return render(request, 'store/moneyrequest.html', {'form': form} )

