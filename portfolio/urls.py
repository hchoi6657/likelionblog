from django.conf.urls import url
import portfolio.views

urlpatterns = [
    url(r'^$', portfolio.views.portfolio, name='portfolio'),
    # url(r'portfolio/', portfolio.views.portfolio, name='portfolio'),    
]
