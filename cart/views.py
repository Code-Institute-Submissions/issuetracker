from django.shortcuts import render, redirect, reverse,get_object_or_404
from packages.models import Package

# Create your views here.
def view_cart(request):
    """ A view that renders the cart contents page"""
    return render(request, "cart.html")
    
def add_to_cart(request, id):
    """ Add a quantity of the specified to the cart"""
    quantity = int(request.POST.get('quantity'))
    cart=request.session.get('cart',{})
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('index'))
    
    
def adjust_cart(request, id):
    """Adjust the quantity of the specified package to the specified amount"""
    package=get_object_or_404(Package, pk=id)
    
    cart = request.session.get('cart',{})
    #cart.remove(package)
    del cart[id]
    request.session['cart'] = cart
    if len(cart)==0:
        return redirect(reverse('index'))
    else:
        return render(request, "cart.html")
