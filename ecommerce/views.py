from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.utils.timezone import localtime
from .models import Customer, Product, Shipping, Payment, Order, ProductOrder
from ecommerce.models import *

# products = [
#     {'id': 1, 'name': 'Porcelain Heart Necklace', 'price': '189,989$', 'description': 'A lucky charm necklace that enhances aura and grants wishes in love.'},
#     {'id': 2, 'name': 'Heart Of The Sea Pearl Necklace', 'price': '1$', 'description': 'A pearl necklace with a heart centerpiece, said to grant control over water.'},
#     {'id': 3, 'name': 'Moonlit Union', 'price': '189,989$', 'description': 'A mystical ring that transforms the wearer into anything they imagine.'},
#     {'id': 4, 'name': 'Argentum Ear Cuff', 'price': '989,999.4499$', 'description': 'An ear cuff that lets you hear hidden frequencies beyond human perception.'}
# ]

# orders = [ชชช
#     {'order_id': '001', 'product_id': 4, 'name': 'Argentum Ear Cuff', 'order_date': '2020-12-20'},
#     {'order_id': '002', 'product_id': 2, 'name': 'Heart Of The Sea Pearl Necklace', 'order_date': '2025-01-11'},
#     {'order_id': '003', 'product_id': 2, 'name': 'Heart Of The Sea Pearl Necklace', 'order_date': '2022-02-22'},
#     {'order_id': '004', 'product_id': 2, 'name': 'Heart Of The Sea Pearl Necklace', 'order_date': '2023-03-03'},
#     {'order_id': '005', 'product_id': 2, 'name': 'Heart Of The Sea Pearl Necklace', 'order_date': '2024-04-04'},
#     {'order_id': '006', 'product_id': 3, 'name': 'Moonlit Union', 'order_date': '2025-05-05'},
#     {'order_id': '007', 'product_id': 1, 'name': 'Porcelain Heart Necklace', 'order_date': '2023-22-11'},
# ]

comments = [
    {'product_id': 1, 'comment': 'Wow! So shiny! I love it!'},
    {'product_id': 1, 'comment': 'Feels super cool when I wear it!'},
    {'product_id': 2, 'comment': 'It’s pretty, but a little too sparkly for me.'},
    {'product_id': 2, 'comment': 'OMG! I feel like a queen in this necklace.'},
    {'product_id': 2, 'comment': 'The pearl is so pretty, but the chain feels a bit weak.'},
    {'product_id': 3, 'comment': 'Totally magical, like something from a fairy tale.'},
    {'product_id': 4, 'comment': 'This ear cuff is amazing! So different from others.'},
    {'product_id': 4, 'comment': 'I feel like I have special powers with this on.'}
]

# Create your views here.
def ecommerce_index_view(request):
    return HttpResponse('Welcome to 6610742493 Patthanan Vachirathatthira views!')

def item_view(request, item_id):
    context_data = {
    "item_id": item_id
    }
    return render(request, 'index.html',context = context_data)

def user_view(request, username):
    try:
        user = User.objects.get(username=username)
        data = {
            "username": user.username,
            "email": user.email,
            "created_at": localtime(user.date_joined).strftime('%d/%m/%Y')
        }
    except User.DoesNotExist:
        data = {"error": "User not found!"}
    return JsonResponse(data)
    
def products_view(request):
    products = Product.objects.all().values("id", "name", "price", "stock", "category")
    return JsonResponse(list(products), safe=False)

def product_by_id(request, id):
    try:
        product = Product.objects.get(id=id)
        data = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock,
            "category": product.category
        }
    except Product.DoesNotExist:
        data = {"error": "Product ID not Found!"}
    return JsonResponse(data)

def comment_products_by_id(request, id):
    comment = [c for c in comments if c['product_id'] == id]
    if comment:
        return JsonResponse(comment, safe=False)
    return JsonResponse({'error': 'Comment not found for this product ID'}, status=404)

def order_by_product_id(request, id):
    product_orders = ProductOrder.objects.filter(product__id=id).select_related("order")
    
    if product_orders.exists():
        data = [
            {
                "order_id": po.order.id,
                "quantity": po.quantity,
                "total_price": po.total_price
            } for po in product_orders
        ]
        return JsonResponse(data, safe=False)
    
    return JsonResponse({"error": "Product or Order ID not Found!"})

def summarize(request):
    summary = {
        'total_products': Product.objects.count(),
        'total_orders': Order.objects.count(),
        'total_users': Customer.objects.count()
    }
    return JsonResponse(summary)

def customer_all_view(request):
    customers = list(Customer.objects.all().values())
    return JsonResponse(customers, safe=False)
    