"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from store import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    success_url = 'home'


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^home/', views.productlist, name='home'),
    url(r'^sellinglist/', views.sellinglist, name='sellinglist'),
    url(r'^boughtlist/', views.boughtlist, name='boughtlist'),
    url(r'^balance/', views.checkbalance, name='checkbalance'),
    #url(r'^addbalance/', views.addbalance, name='addbalance'),
    url(r'^product/(?P<pk>\d+)/remove/$', views.productremove, name='product_remove'),
    url(r'^product/(?P<pk>\d+)/details/$', views.productdetails, name='product_details'),
    url(r'^product/(?P<pk>\d+)/buy/$', views.buyproduct, name='buyproduct'),
    url(r'^addproduct/', views.addproduct, name='addproduct'),
    url(r'^moneyrequest/', views.moneyrequest, name='moneyrequest'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)