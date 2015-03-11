from django.conf.urls import patterns, include, url
from apiserver import views

urlpatterns = patterns('',
    url(r'^user/(\w+)/(\w+)', views.login),
    url(r'^userlist', views.user_list),
    url(r'^perm/(\w+)/(\w+)', views.perm),
)
