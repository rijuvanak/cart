from django.shortcuts import render
from .models import Product, Order

def process_cart(request):
    if request.method == 'POST':
        # Retrieve the form data
        product_a_quantity = int(request.POST.get('product_a_quantity', 0))
        product_a_gift_wrap = request.POST.get('product_a_gift_wrap', False)
        product_b_quantity = int(request.POST.get('product_b_quantity', 0))
        product_b_gift_wrap = request.POST.get('product_b_gift_wrap', False)
        product_c_quantity = int(request.POST.get('product_c_quantity', 0))
        product_c_gift_wrap = request.POST.get('product_c_gift_wrap', False)

        # Create an order object
        order = Order(
            product_a_quantity=product_a_quantity,
            product_a_gift_wrap=product_a_gift_wrap,
            product_b_quantity=product_b_quantity,
            product_b_gift_wrap=product_b_gift_wrap,
            product_c_quantity=product_c_quantity,
            product_c_gift_wrap=product_c_gift_wrap
        )

        # Calculate order details
        product_a_price = Product.objects.get(name='Product A').price
        product_b_price = Product.objects.get(name='Product B').price
        product_c_price = Product.objects.get(name='Product C').price

        product_a_total = product_a_quantity * product_a_price
        product_b_total = product_b_quantity * product_b_price
        product_c_total = product_c_quantity * product_c_price

        cart_total = order.get_cart_total()
        discount_name, discount_amount = order.get_discount()
        gift_wrap_fee = order.get_gift_wrap_fee()
        shipping_fee = order.get_shipping_fee()
        total = cart_total - discount_amount + gift_wrap_fee + shipping_fee

        # Render the results in a template
        return render(request, 'result.html', {
            'order': order,
            'product_a_quantity': product_a_quantity,
            'product_a_total': product_a_total,
            'product_b_quantity': product_b_quantity,
            'product_b_total': product_b_total,
            'product_c_quantity': product_c_quantity,
            'product_c_total': product_c_total,
            'cart_total': cart_total,
            'discount_name': discount_name,
            'discount_amount': discount_amount,
            'gift_wrap_fee': gift_wrap_fee,
            'shipping_fee': shipping_fee,
            'total': total
        })

    # If the request method is not POST, render the form
    return render(request, 'catalog.html', {
        'products': Product.objects.all()
    })

    # If the request method is not POST, render the form
    return render(request, 'catalog.html', {
        'products': Product.objects.all()
    })
