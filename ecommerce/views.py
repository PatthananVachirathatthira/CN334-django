from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_view(request):
    return HttpResponse('Welcome to 6610742493 Patthanan Vachirathatthira views!')

def item_view(request, item_id):
    context_data = {
    "item_id": item_id
    }
    return render(request, 'index.html',context = context_data)