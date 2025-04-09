from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Sample book data with prices
BOOKS = [
    {"id": 1, "title": "The Alchemist", "author": "Paulo Coelho", "price": 299},
    {"id": 2, "title": "Atomic Habits", "author": "James Clear", "price": 350},
    {"id": 3, "title": "Python Crash Course", "author": "Eric Matthes", "price": 599},
    {"id": 4, "title": "Deep Work", "author": "Cal Newport", "price": 450},
    {"id": 5, "title": "1984", "author": "George Orwell", "price": 199},
    {"id": 6, "title": "Sapiens", "author": "Yuval Noah Harari", "price": 499},
    {"id": 7, "title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "price": 349},
    {"id": 8, "title": "Clean Code", "author": "Robert C. Martin", "price": 579},
    {"id": 9, "title": "Zero to One", "author": "Peter Thiel", "price": 289},
    {"id": 10, "title": "The Lean Startup", "author": "Eric Ries", "price": 399},
]

# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'store/signup.html', {'form': form})

# Book list view
@login_required
def book_list(request):
    return render(request, 'store/book_list.html', {'books': BOOKS})

# Add to cart view
@login_required
def add_to_cart(request, book_id):
    cart = request.session.get('cart', [])
    if book_id not in cart:
        cart.append(book_id)
    request.session['cart'] = cart
    return redirect('book_list')

# Remove from cart view
@login_required
def remove_from_cart(request, book_id):
    cart = request.session.get('cart', [])
    if book_id in cart:
        cart.remove(book_id)
    request.session['cart'] = cart
    return redirect('view_cart')

# View cart
@login_required
def view_cart(request):
    cart = request.session.get('cart', [])
    cart_books = [book for book in BOOKS if book['id'] in cart]
    total_price = sum(book['price'] for book in cart_books)
    return render(request, 'store/cart.html', {
        'cart_books': cart_books,
        'total_price': total_price
    })
