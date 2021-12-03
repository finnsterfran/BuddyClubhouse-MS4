from django.db.models.signals import post_save, post_delete
from .models import OrderLineItem


def update_on_save(sender, instance, created, **kwargs):
    """ Update order total on lineitem update/create """
    instance.order.update_total()

def update_on_delete(sender, instance, **kwargs):
    """ Update order total on lineitem delete """
    instance.order.update_total()

post_save.connect(update_on_save, sender=OrderLineItem)
post_delete.connect(update_on_delete, sender=OrderLineItem)
