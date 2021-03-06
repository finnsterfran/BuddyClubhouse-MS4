import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from users.models import Profile
from contribution.models import Donation


class Order(models.Model):
    """ Model to store order information """
    order_number = models.CharField(max_length=32,
                                    null=False,
                                    editable=False)
    username = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name='orders')
    first_name = models.CharField(max_length=200,
                                  null=False,
                                  blank=False)
    last_name = models.CharField(max_length=200,
                                 null=False,
                                 blank=False)
    email = models.EmailField(max_length=200,
                              null=False,
                              blank=False)
    address_line_1 = models.CharField(max_length=80,
                                      null=False,
                                      blank=False)
    address_line_2 = models.CharField(max_length=80,
                                      null=True,
                                      blank=True)
    postal_code = models.CharField(max_length=20,
                                   null=True,
                                   blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      null=False,
                                      default=0)
    grand_total = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      null=False,
                                      default=0)
    original_cart = models.TextField(null=False,
                                     blank=False,
                                     default='')
    stripe_pid = models.CharField(max_length=254,
                                  null=False,
                                  blank=False,
                                  default='')

    def _generate_order_number(self):
        """ Generate a random order number using UUID """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Update grand total each time a line item has been added """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        """ Override the original save method to set the order number
            if order number has yet to be created """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False,
                              blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Donation, null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False,
                                   default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False,
                                         blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """ Override the original save method to get the lineitem total
            and update the order total """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'INFO {self.product.name} on order {self.order.order_number}'
