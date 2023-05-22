from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Order(models.Model):
    product_a_quantity = models.PositiveIntegerField(default=0)
    product_a_gift_wrap = models.BooleanField(default=False)
    product_b_quantity = models.PositiveIntegerField(default=0)
    product_b_gift_wrap = models.BooleanField(default=False)
    product_c_quantity = models.PositiveIntegerField(default=0)
    product_c_gift_wrap = models.BooleanField(default=False)

    def get_cart_total(self):
        product_a_price = Product.objects.get(name='Product A').price
        product_b_price = Product.objects.get(name='Product B').price
        product_c_price = Product.objects.get(name='Product C').price

        cart_total = (
            self.product_a_quantity * product_a_price +
            self.product_b_quantity * product_b_price +
            self.product_c_quantity * product_c_price
        )
        return cart_total

    def get_discount(self):
        cart_total = self.get_cart_total()

        if cart_total > 200:
            discount_amount = 10
            discount_name = "flat_10_discount"
        elif (
            self.product_a_quantity > 10 or
            self.product_b_quantity > 10 or
            self.product_c_quantity > 10
        ):
            discount_amount = cart_total * 0.05
            discount_name = "bulk_5_discount"
        elif self.get_total_quantity() > 20:
            discount_amount = cart_total * 0.1
            discount_name = "bulk_10_discount"
        elif (
            self.get_total_quantity() > 30 and
            (
                self.product_a_quantity > 15 or
                self.product_b_quantity > 15 or
                self.product_c_quantity > 15
            )
        ):
            discount_amount = self.get_excess_product_total() * 0.5
            discount_name = "tiered_50_discount"
        else:
            discount_amount = 0
            discount_name = ""

        return discount_name, discount_amount

    def get_total_quantity(self):
        return (
            self.product_a_quantity +
            self.product_b_quantity +
            self.product_c_quantity
        )

    def get_excess_product_total(self):
        excess_total = 0
        product_a_price = Product.objects.get(name='Product A').price
        product_b_price = Product.objects.get(name='Product B').price
        product_c_price = Product.objects.get(name='Product C').price

        if self.product_a_quantity > 15:
            excess_total += (self.product_a_quantity - 15) * product_a_price

        if self.product_b_quantity > 15:
            excess_total += (self.product_b_quantity - 15) * product_b_price

        if self.product_c_quantity > 15:
            excess_total += (self.product_c_quantity - 15) * product_c_price

        return excess_total

    def get_gift_wrap_fee(self):
        gift_wrap_fee = (
            self.product_a_quantity +
            self.product_b_quantity +
            self.product_c_quantity
        )
        return gift_wrap_fee

    def get_shipping_fee(self):
        packages = (self.get_total_quantity() + 9) // 10
        shipping_fee = packages * 5
        return shipping_fee
