from ..models import Driver

def list_drivers(**filters):
    """
    Get list of drivers by filters
    """
    return Driver.objects.filter(**filters)

def get_driver(**filters):
    """
    Get single driver by filters
    """
    return Driver.objects.get(**filters)