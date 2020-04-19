from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.trainer, name='trainer'),
    url(r'^trainer/delete/(?P<value>.*)/$', views.delete_user, name='deleteUser'),
]