import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from supplyproject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


# Create your views here.


def index(request):
    return render(request, 'index.html')


def footer(request):
    return render(request, 'footer.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def terms(request):
    return render(request, 'terms.html')


def register(request):
    if request.method == 'POST':
        a = regform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['name']
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            cp = a.cleaned_data['password2']
            mb = a.cleaned_data['mobile']
            ad = a.cleaned_data['address']
            if ps == cp:
                b = regmodel(name=nm, email=em, password=ps, mobile=mb, address=ad)
                b.save()
                return redirect(login)
            else:
                return redirect(passfail)
                # return HttpResponse("Incorrect password")
        else:
            return HttpResponse("Registration failed")
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        a = logform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = regmodel.objects.all()
            for i in b:
                request.session['id'] = i.id
                print(request.session['id'])

                # print(id)
                if i.email == em and i.password == ps:
                    return redirect(feeddisplay)


            else:
                # return HttpResponse("Login failed")
                return redirect(failed)
    else:
        return render(request, 'login.html')


def shopregister(request):
    if request.method == 'POST':
        a = shopregform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['name']
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            cp = a.cleaned_data['password2']
            mb = a.cleaned_data['mobile']
            ad = a.cleaned_data['address']
            if ps == cp:
                b = shopregmodel(name=nm, email=em, password=ps, mobile=mb, address=ad)
                b.save()
                return redirect(login)
            else:
                return redirect(passfail)
                # return HttpResponse("Incorrect password")
        else:
            return HttpResponse("Registration failed")
    return render(request, 'shopregister.html')


def shoplogin(request):
    if request.method == 'POST':
        a = shoplogform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = shopregmodel.objects.all()
            for i in b:

                # print(id)
                if i.email == em and i.password == ps:
                    # return HttpResponse("Login success")
                    return redirect(productdisplay)

            else:
                return redirect(passfail)
                # return HttpResponse("Login failed")

    else:
        return render(request, 'shoplogin.html')


def productdetails(request):
    if request.method == 'POST':
        a = productform(request.POST, request.FILES)
        if a.is_valid():
            nm = a.cleaned_data['name']
            pr = a.cleaned_data['price']
            im = a.cleaned_data['image']

            b = productmodel(name=nm, price=pr, image=im)
            b.save()
            # return HttpResponse("File upload success")
            return redirect(productdisplay)
        else:
            return render(failed)
            # return HttpResponse("File upload failed")
    else:
        return render(request, 'productdetails.html')


def productdisplay(request):
    a = productmodel.objects.all()
    namelist = []
    pricelist = []
    imagelist = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        img = i.image
        imagelist.append(str(img).split('/')[-1])
        nm = i.name
        namelist.append(nm)
        pl = i.price
        pricelist.append(pl)
    mylist = zip(imagelist, namelist, pricelist, id)
    return render(request, 'productdisplay.html', {'list': mylist})


def deleteproduct(request, id):
    a = productmodel.objects.get(id=id)
    if len(a.image) > 0:
        os.remove(a.image.path)
    a.delete()
    return redirect(productdisplay)


def editproduct(request, id):
    a = productmodel.objects.get(id=id)
    image = str(a.image).split('/')[-1]
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(a.image) > 0:
                os.remove(a.image.path)
            a.image = request.FILES['image']
        a.name = request.POST.get('name')
        a.price = request.POST.get('price')
        # a.description = request.POST.get('description')
        a.save()
        return redirect(productdisplay)
    return render(request, 'editproduct.html', {'a': a, 'image': image})


def userprofile(request):
    a = productmodel.objects.all()
    namelist = []
    pricelist = []
    imagelist = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        img = i.image
        imagelist.append(str(img).split('/')[-1])
        nm = i.name
        namelist.append(nm)
        pl = i.price
        pricelist.append(pl)
    mylist = zip(imagelist, namelist, pricelist, id)
    return render(request, 'userprofile.html', {'list': mylist})


def wishlist(request, id):
    a = productmodel.objects.get(id=id)
    id1 = request.session['id']
    b = wishlistmodel(uid=id1, pid=id, name=a.name, price=a.price, image=a.image)
    b.save()
    return redirect(mywish)


def mywish(request):
    a = wishlistmodel.objects.all()
    namelist = []
    pricelist = []
    imagelist = []

    id = []
    uid = []

    for i in a:
        ui = i.uid
        uid.append(ui)
        id1 = i.id
        id.append(id1)
        img = i.image
        imagelist.append(str(img).split('/')[-1])
        nm = i.name
        namelist.append(nm)
        pl = i.price
        pricelist.append(pl)
    ui = request.session['id']
    mylist = zip(imagelist, namelist, pricelist, id, uid)
    return render(request, 'mywish.html', {'mylist': mylist, 'id': ui})


def removewish(request, id):
    a = wishlistmodel.objects.get(id=id)
    a.delete()
    return redirect(mywish)


def cart(request, id):
    a = productmodel.objects.get(id=id)
    id1 = request.session['id']
    print(id1)
    b = cartmodel(uid=id1, pid=id, name=a.name, price=a.price, image=a.image)
    b.save()
    return redirect(mycart)


def mycart(request):
    a = cartmodel.objects.all()
    namelist = []
    pricelist = []
    imagelist = []

    id = []
    u = []
    for i in a:
        ui = i.uid
        u.append(ui)
        id1 = i.id
        id.append(id1)
        img = i.image
        imagelist.append(str(img).split('/')[-1])
        nm = i.name
        namelist.append(nm)
        pl = i.price
        pricelist.append(pl)
    ab = request.session['id']
    print(ab)
    mylist = zip(imagelist, namelist, pricelist, id, u)
    return render(request, 'mycart.html', {'mylist': mylist, 'ab': ab})


def removecart(request, id):
    a = cartmodel.objects.get(id=id)
    a.delete()
    return redirect(mycart)


def wishlisttocart(request, id):
    a = wishlistmodel.objects.get(id=id)
    b = cartmodel(image=a.image, name=a.name, price=a.price, pid=a.pid,uid=a.uid)
    b.save()
    # return HttpResponse("Product added to Cart")
    return redirect(mycart)


def vieworder(request):
    a = buymodel.objects.all()
    return render(request, 'vieworder.html', {'a': a})


def buy(request, id):
    b = cartmodel.objects.get(id=id)
    nm = b.name
    pr = b.price
    if request.method == 'POST':
        a = buyform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['name']
            pr = int(a.cleaned_data['price'])
            fn = a.cleaned_data['fname']
            ad = a.cleaned_data['address']
            em = a.cleaned_data['email']
            nmb = a.cleaned_data['number']
            pm = a.cleaned_data['paymode']
            qa = int(a.cleaned_data['quantity'])
            b = buymodel(name=nm, price=pr, fname=fn, address=ad, email=em, number=nmb, paymode=pm, quantity=qa)
            b.save()
            total = qa * pr
            subject = f"Order Placed for {nm}"
            message = f"Hello {fn} ,\n \t  your order for our product  {nm} has been placed successfully. You can expect delivery within 4 days." \
                      f"\n\n Order Details:\n Product Name: {nm}\n Price for 1 piece : {pr} Rupees \n Quantity: {qa} \n\n\n Customer details:\n Name: {fn}\n Address: {ad}\n Email: {em} \n Number: {nmb}\n Payment Mode: {pm}\n Total amount to be paid : {total}"
            email_from = EMAIL_HOST_USER
            send_mail(subject, message, email_from, [em])
            return render(request, 'bill.html', {'fn': fn, 'total': total, 'nm': nm, 'qa': qa, 'pm': pm, 'pr': pr})

        else:
            return render(request, 'failed.html')
    else:
        return render(request, 'buy.html', {'nm': nm, 'pr': pr})


def success(request):
    return render(request, 'success.html')


def failed(request):
    return render(request, 'failed.html')


def passfail(request):
    return render(request, 'passfail.html')


def bill(request):
    return render(request, 'bill.html')


def feed(request):
    if request.method == 'POST':
        a = feedform(request.POST, request.FILES)
        if a.is_valid():
            ct = a.cleaned_data['content']
            im = a.cleaned_data['image']
            b = feedmodel(content=ct,image=im)
            b.save()
            # return HttpResponse("File upload success")
            return redirect(feedsuccess)
        else:
            return redirect(failed)
            # return HttpResponse("File upload failed")
    else:
        return render(request, 'feed.html')


def feeddisplay(request):
    a = feedmodel.objects.all()
    contentlist = []

    imagelist = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        img = i.image
        imagelist.append(str(img).split('/')[-1])
        ct = i.content
        contentlist.append(ct)
    mylist = zip(imagelist, contentlist,  id)
    return render(request, 'feeddisplay.html', {'list': mylist})



def feedsuccess(request):
    return render(request,'feedsuccess.html')