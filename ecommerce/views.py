from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

products = [
    {'id': 1, 'name': 'Porcelain Heart Necklace', 'price': '189,989$', 'description': 'A lucky charm necklace that enhances aura and grants wishes in love.'},
    {'id': 2, 'name': 'Heart Of The Sea Pearl Necklace', 'price': '1$', 'description': 'A pearl necklace with a heart centerpiece, said to grant control over water.'},
    {'id': 3, 'name': 'Moonlit Union', 'price': '189,989$', 'description': 'A mystical ring that transforms the wearer into anything they imagine.'},
    {'id': 4, 'name': 'Argentum Ear Cuff', 'price': '989,999.4499$', 'description': 'An ear cuff that lets you hear hidden frequencies beyond human perception.'}
]

orders = [
    {'order_id': '001', 'product_id': 4, 'name': 'Argentum Ear Cuff', 'order_date': '2020-12-20'},
    {'order_id': '002', 'product_id': 2, 'name': 'Heart Of The Sea Pearl Necklace', 'order_date': '2025-01-11'},
    {'order_id': '003', 'product_id': 2, 'name': 'Heart Of The Sea Pearl Necklace', 'order_date': '2022-02-22'},
    {'order_id': '004', 'product_id': 2, 'name': 'Heart Of The Sea Pearl Necklace', 'order_date': '2023-03-03'},
    {'order_id': '005', 'product_id': 2, 'name': 'Heart Of The Sea Pearl Necklace', 'order_date': '2024-04-04'},
    {'order_id': '006', 'product_id': 3, 'name': 'Moonlit Union', 'order_date': '2025-05-05'},
    {'order_id': '007', 'product_id': 1, 'name': 'Porcelain Heart Necklace', 'order_date': '2023-22-11'},
]

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
    users = {
        'username': username, 
        'email': f'{username}@gmail.com', 
        'signup_date': '2024-01-01'
    }
    return JsonResponse(users)
    
def products_view(request):
    return JsonResponse(products, safe=False)

def product_by_id(request, id):
    product = next((p for p in products if p['id'] == id), None)
    if product:
        return JsonResponse(product)
    return JsonResponse({'error':'product not found'}, status=404)

def comment_products_by_id(request, id):
    comment = [c for c in comments if c['product_id'] == id]
    if comment:
        return JsonResponse(comment, safe=False)
    return JsonResponse({'error': 'Comment not found for this product ID'}, status=404)

def summarize(request):
    summary = {
        'total_products': len(products),
        'total_orders': len(orders),
        'total_comments': len(comments)
    }
    return JsonResponse(summary)

    