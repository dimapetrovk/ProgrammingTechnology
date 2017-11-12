from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  # url(r'^auth/login/', obtain_jwt_token),

                  url(r'^login/$', auth_views.login, name='login'),
                  url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
                  # url(r'^auth/refresh/', refresh_jwt_token),
                  url(r'^i18n/', include('django.conf.urls.i18n')),
                  url(r'^', include('auto_base.urls'), name='home'),
              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
