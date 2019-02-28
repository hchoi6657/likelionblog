from django.conf.urls import url
import blogapp.views

urlpatterns = [
    url(r'blog/new/', blogapp.views.new, name='new'),
    url(r'blog/create/', blogapp.views.create, name='create'),
    url(r'blog/(?P<blog_id>[0-9]+)$', blogapp.views.detail, name='detail'),
    url(r'blog/delete/(?P<blog_id>[0-9]+)', blogapp.views.destroy, name='destroy'),
    url(r'^$', blogapp.views.blog, name='blog'),
]
