from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil
from datetime import datetime
from django.contrib import messages
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from .models import Orders


@csrf_exempt
def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        cart = request.session.get('cart', {})
        cart[product_id] = cart.get(product_id, 0) + 1
        request.session['cart'] = cart
        return HttpResponse('Added to cart')
    return HttpResponse(status=400)

def cart(request):
    products = Product.objects.all()
    product_data = {
        str(p.id): {
            'name': p.product_name,
            'price': p.price,
            'image': p.image.url if p.image else ''
        }
        for p in products
    }
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '{}')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        address = address1 + " " + address2
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')

        # Save order
        order = Orders(
            items_json=items_json,
            name=name,
            email=email,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code
        )
        order.save()
        return render(request, 'shop/order_success.html', {'order_id': order.order_id})

    return render(request, 'shop/cart.html', {'products_json': json.dumps(product_data)})

def index(request):
    
    # products= Product.objects.all()
    # n= len(products)
    # nSlides= n//4 + ceil((n/4)-(n//4))
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item['category'] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n= len(prod)
        nSlides= n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params={'allProds':allProds }
    return render(request,"shop/index.html", params)

def you(request):
    return render(request, 'shop/you.html')

def basic(request):
    return render(request, 'shop/basic.html')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact =Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(request, "Your message has been sent")

    return render(request,"shop/contact.html")

def about(request):
    return render(request, 'shop/about.html')


def search(request):
    query = request.GET.get('query', '')
    products = []
    if query:
        products = Product.objects.filter(product_name__icontains=query) | Product.objects.filter(desc__icontains=query) | Product.objects.filter(category__icontains=query)
    return render(request, 'shop/search.html', {'products': products, 'query': query})

def productView(request, myid):
    product= Product.objects.filter(id=myid)
    return render(request, 'shop/productView.html' , {'product': product[0]})


