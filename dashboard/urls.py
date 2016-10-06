from django.conf.urls import url

from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^devices/?$', views.devices, name='devices'),
    url(r'^devices/(?P<device_id>[0-9]+)$', views.device, name='device'),
    url(r'^devices/(?P<device_id>[0-9]+)/change_label/$', views.device_change_label, name='device_change_label'),
]
