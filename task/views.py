from django.shortcuts import render,redirect
from .models import book
# Create your views here.
def home(request):
    all=book.objects.all()
    return render(request,'index.html',{'all':all})

def create_form(request):
    if request.method=="POST":
        name=request.POST['book_name']
        a_name=request.POST['a_name']
        price=request.POST['price']
        id=None
        obj=book(id,name=name,a_name=a_name,price=price)
        obj.save()
        return render(request,"index.html")
    else:
        return render(request,'create.html')

def update_form(request,id):
    if request.method=="POST":
        name = request.POST['book_name']
        a_name = request.POST['a_name']
        price =request.POST['price']
        a = book.objects.get(id=id)
        a.name =name
        a.a_name = a_name
        a.price=price
        a.save()
        return redirect('/')
    else:
        obj = book.objects.get(id=id)
        return render(request,'update.html',{'obj':obj})