from django.shortcuts import render,HttpResponse,redirect
from .models import Category,Product,User,Cart,PlaceOrder
from .forms import UserForm
from django.contrib.auth import login,logout,authenticate


def index(request):
    plist=Product.objects.all()
    cl=Category.objects.all()
    d={'cl':cl,'pl':plist}
    return render(request,'index.html',d)

#get product by category
def getByCategory(request,id):
    pl=Product.objects.filter(category=id)
    cl=Category.objects.all()
    d={'cl':cl,'pl':pl}
    return render(request,'index.html',d)

# user registration function
def addUser(request):
    if request.method=='POST':
        f=UserForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=UserForm
        pl=Product.objects.all()
        cl=Category.objects.all()
        d={'cl':cl,'pl':pl,'form':f}
        return render(request,'forms.html',d)

# user Login
def login_view(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        usr=authenticate(request,username=uname,password=passw)
        if usr is not None:
            request.session['uid']=usr.id
            login(request,usr)
            return redirect('/')
        else:
            return HttpResponse("<h1>InValid UserName and Password</h1>")
    else:
        pl=Product.objects.all()
        cl=Category.objects.all()
        d={'cl':cl}
        return render(request,'login.html',d)


#user Logout
def logout_view(request):
    logout(request)
    return redirect('/')


# search product
def search(request):
    cl=Category.objects.all()

    if request.method=='POST':
        pname=request.POST.get('shr')
        pl=Product.objects.filter(name__icontains=pname)  
        d={'cl':cl,'pl':pl}
        return render(request,'search.html',d)
    else:
        pl=Product.objects.all() 
        d={'cl':cl,'pl':pl}
        return render(request,'search.html',d)

# add product in cart
def addToCart(request,id):
    cart=Cart()
    pd=Product.objects.get(id=id)
    print('------->',pd)
    cart.product=pd
    uid=request.session.get('uid')
    usr=User.objects.get(id=uid)
    print('------------> ',usr)
    cart.user=usr
    cart.save()
    return redirect('/')


# show user cart
def cartlist(request):
    uid=request.session.get('uid')
    if request.method=='POST':
        odr=PlaceOrder()
        totalBill=request.POST.get('totalBill')
        print('--------------> ',totalBill)
        usr=User.objects.get(id=uid)
        odr.totalBill=totalBill
        odr.user=usr
        if odr is not None:
            odr.save()
            clist=Cart.objects.filter(user_id=uid)
            for i in clist:
                i.delete()
            return redirect('/')
        else:
            return HttpResponse("Error in CART List Delete Operations")
    else:
       
        clist=Cart.objects.filter(user_id=uid)
        cl=Category.objects.all()
        totalBill=0
        for i in clist:
            totalBill=totalBill+i.product.price
        d={'cl':cl,'clist':clist,'totalBill':totalBill}
        return render(request,'cartList.html',d)
    

# user orderProduct List
def getOrderList(request,id):
    ol=PlaceOrder.objects.filter(user_id=id)
    cl=Category.objects.all()
    d={'ol':ol,'cl':cl}
    return render(request,'orderList.html',d)


