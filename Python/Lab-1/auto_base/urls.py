from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

try:
  from django.conf.urls import patterns
except ImportError:
  pass
from auto_base import views
urlpatterns = [
    url(r'^api/driver/(?P<id>[0-9]+)$', views.DriverAPIView.as_view()),
    url(r'^api/driver/$', views.DriverAPIListView.as_view()),

    url(r'^api/order/(?P<id>[0-9]+)$', csrf_exempt(views.OrderAPIView.as_view())),

    url(r'^auth/register/', views.RegistrationAPIView.as_view()),
    url(r'^sign_in/', views.SignInFormView.as_view()),

     url(r'^order/(?P<pk>\d+)$', views.OrderDetailView.as_view()),

    url(r'^$', views.OrderListView.as_view()),
]

