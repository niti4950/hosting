"""amado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from amadoapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index,name='index'),
    url(r'^checkout/$',checkout,name='checkout'),
    url(r'^shop/$',shop,name='shop'),
    url(r'^login1/$',login1,name='login1'),
    url(r'^search/$',search,name='search'),
    #http://127.0.0.1:8000/shop/tables/
    url(r'^shop/(\w+)/$',Single_category,name='category'),
    url(r'^product_detail/(\d+)/$',product_detail,name='detail'),
    url(r'^cart_detail/$',cart_detail,name='cart'),
    url(r'^login/$',login,name='login'),
    url(r'^signup/$',sign_up,name='signup'),
    url(r'^delete/(\d+)/$',delete_item,name='delete')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
