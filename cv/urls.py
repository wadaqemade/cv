from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='base.html'), name='base'), # new

]
