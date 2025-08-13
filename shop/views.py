from django.shortcuts import render,redirect
from .models import Products,Order
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    # Search functionality
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = Products.objects.filter(title__icontains=item_name)
    else:
        product_objects = Products.objects.all()

    # Pagination
    paginator = Paginator(product_objects, 4)  # Show 4 products per page
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'Product_objects': product_objects})


# Detail view 
def detail(request,id):
    product_object=Products.objects.get(id=id)
    return render(request,'shop/detail.html', {'product_object':product_object})

def order_success(request):
    return render(request, 'shop/order_success.html')

def buy_now(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = get_object_or_404(Product, id=product_id)

        # Save only this product in session
        request.session['buy_now_item'] = {
            'id': product.id,
            'name': product.name,
            'price': float(product.price),
            'quantity': 1
        }
        return redirect('checkout')

    return redirect('index')  # fallback if accessed directly


# checkout
def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        address2 = request.POST.get('address2', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zipcode = request.POST.get('zipcode', "")
        total=request.POST.get('total',"")

        order = Order(
            name=name,
            email=email,
            address=address,
            address2=address2,
            city=city,
            state=state,
            zipcode=zipcode,
            total=total
        )
        order.save()
        return redirect('order_success')

    return render(request, 'shop/checkout.html')




