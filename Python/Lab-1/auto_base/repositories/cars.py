from ..models import Car

def list_cars(**filters):
    """
    Get list of cars by filters
    """
    return Car.objects.filter(**filters)

def get_car(**filters):
    """
    Get single car by filters
    """
    return Car.objects.get(**filters)