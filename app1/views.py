from django.shortcuts import render , redirect
from .models import *
import bcrypt
from django.contrib import messages


def main(request):
    return render(request, 'main.html')

def login(request):
    return render(request, "login.html")


def login_form(request):
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.filter(email=email).first()
    if user:
        if bcrypt.checkpw(password.encode(), user.password.encode()):
            request.session['user_id'] = user.id
            return redirect('/')
    messages.error(request, 'Invalid Credentials')
    return redirect('/login')


def register(request):
    return render(request, "register.html")


def registration(request):
    errors = User.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/register')
    else:
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name=fname, last_name=lname,email=email, password=hashed)
        user = User.objects.last()
        request.session['user_id'] = user.id
    return redirect('/')

def boys(request):
    boys_clothes=Cloth.objects.all()
    context={
        'boys_clothes':boys_clothes,
    }
    return render(request,'boy.html',context)

def girls(request):
    girls_clothes=Cloth.objects.all()
    context={
        'girls_clothes':girls_clothes,
    }
    return render(request,'girl.html',context)

def view_cloth(request,id):
    context={
        'cloth':Cloth.objects.get(id=id),
    }
    return render(request,'view.html',context)




def admin(request):
    return render(request,'admin.html')



def create_cloth(request):
    errors = Cloth.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        size=request.POST['size']
        gender=request.POST['gender']
        pic_src=request.POST['pic_source']
        description=request.POST['description']
        price=request.POST['price']
        quantity=request.POST['quantity']
        Cloth.objects.create(size=size, gender=gender, pic_src=pic_src,description=description, price=price, quantity=quantity)
        cloth=Cloth.objects.last()
        if cloth.gender == 'boys':
            return redirect('/boys')
        else:
            return redirect('/girls')

def add_to_cart(request,id):
    if 'user_id' not in request.session:
        return redirect('/login')
    user=User.objects.get(id=request.session['user_id'])
    Clothorder.objects.create(user=user,cloth=Cloth.objects.get(id=id),quantity=int(request.POST['quantity']))
    return redirect('/cart')

# def cart(request):
#     user=User.objects.get(id=request.session['user_id'])
#     order=Order.objects.filter(user=user)
#     total_items=sum([oc.quanity for oc in order.ordercloth_set.all()])
#     total_price=sum([oc.quanity * oc.cloth.price  for oc in order.ordercloth_set.all()])
#     context={
#         'all_cloth_orders':order.orderclothes.all(),
#         'total_items':total_items,
#         'total_price':total_price
#     }
#     return render(request,'cart.html',context)

def cart(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    user = User.objects.get(id=request.session['user_id'])
    ordered_clothes = user.clothorders.all() # filter OrderCloth objects by order id
    total_items = sum([oc.quantity for oc in user.clothorders.all()])
    total_price = sum([oc.quantity * oc.cloth.price for oc in user.clothorders.all()])
    context = {
        'all_cloth_orders': ordered_clothes,
        'total_items': total_items,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)

def checkout(request):
    user = User.objects.get(id=request.session['user_id'])
    total_items = sum([oc.quantity for oc in user.clothorders.all()])
    total_price = sum([oc.quantity * oc.cloth.price for oc in user.clothorders.all()])
    context = {
        'total_items': total_items,
        'total_price': total_price
    }
    return render(request, "checkout.html",context)

def submit_order(request):
    errors = Address.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/checkout')
    else:
        user = User.objects.get(id=request.session['user_id'])
        ordered_clothes = user.clothorders.all()
        ordered_clothes.delete()
        Address.objects.create(phone_num=request.POST['phone'],city=request.POST['city'],street=request.POST['street'],user=user)
        return redirect('/order_success')

def order_success(request):
    return render(request, 'order_success.html')    

def delete_users(request):
    # User.objects.all().delete()
    # Address.objects.all().delete()
    # Clothorder.objetcs.all().delete()
    # Cloth.objects.all().delete()
    del request.session['user_id']
    return redirect('/')

def edit_quantity(request,id):
    cloth_order=Clothorder.objects.get(id=id)
    quantity=request.POST['quantity']
    cloth_order.quantity=quantity
    cloth_order.save()
    return redirect('/cart')

def delete(request,id):
    cloth_order=Clothorder.objects.get(id=id)
    cloth_order.delete()
    return redirect('/cart')

