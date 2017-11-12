"""
Views for rendering
"""

from django.views.generic import TemplateView
from ..repositories import orders as orders_repository
from ..repositories import cars as car_repository
from ..repositories import drivers as driver_repository


class OrderListView(TemplateView):
    """
    Render order list only for current driver
    """

    template_name = 'order_list.html'

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        try:
            driver = driver_repository.get_driver(user=self.request.user)
            car = car_repository.list_cars(driver=driver)
            context['orders'] = orders_repository.list_orders(car=car)
        except:
            return context
        return context


class OrderDetailView(TemplateView):
    """
    Render order report form
    """

    template_name = 'order_details.html'

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context['order'] = orders_repository.get_order(pk=kwargs['pk'])
        context['user'] = self.request.user
        return context


class SignInFormView(TemplateView):
    """
    Render sign in form
    """
    template_name = 'sign_in_form.html'
