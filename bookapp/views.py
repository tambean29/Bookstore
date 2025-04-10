from django.shortcuts import render,redirect
from .models import Books
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def load_books(request):
    books = Books.objects.all()
    template = loader.get_template('home.html')
    context = {
        'books':books
    }
    return HttpResponse(template.render(context, request))

def add_to_cart(request):
    template = loader.get_template('home.html')
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        book = Books.objects.get(id=book_id)
        cart = request.session.get('cart', [])
        cart.append({'id': book.id, 'bookname': book.bookname, 'author': book.author, 'price': float(book.price)})
        request.session['cart'] = cart
        context = {"message":"Book added to cart"}
        return redirect('view_cart')
    else:
        context = {"message":"Invalid request"}
        return HttpResponse(template.render(context, request))

def view_cart(request):
    template = loader.get_template('cart.html')
    cart = request.session.get('cart',[])
    print("Cart:",cart)
    if cart:
        try:
            total_price = sum(item['price'] for item in cart)
            context = {
                'cart': cart,
                'total_price': total_price
            }
            return HttpResponse(template.render(context,request))
        except Exception as e:
            print("Error calculating total price:", e)
            context = {
                'cart': cart,
                'total_price': 0
            }
            return redirect('clear_cart')
    else:
        context = {
            'message': 'Your cart is empty.'
        }
        return HttpResponse(template.render(context, request))
def clear_cart(request):
    request.session['cart'] = []
    return redirect('view_cart')