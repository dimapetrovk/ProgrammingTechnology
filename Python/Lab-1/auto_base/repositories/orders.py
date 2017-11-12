from ..models import Order

def list_orders(**filters):
    """
    Get list of orders by filters
    """
    return Order.objects.filter(**filters)

def get_order(**filters):
    """
    Get single order by filters
    """
    return Order.objects.get(**filters)