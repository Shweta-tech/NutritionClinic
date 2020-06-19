"""nutritionforms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$',views.base,name=''),
    url(r'^forms/$',views.form,name='forms'),
    url(r'^childregter/$',views.childregter,name='childregter'),
    url(r'^login/$',views.login,name='login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^breastfeed/$',views.breastfeed,name='breastfeed'),
    url(r'^brestfed/$',views.brestfed,name='brestfed'),
    url(r'^pre_delivery/$',views.pre_delivery,name='pre_delivery'),
    url(r'^follow_up/$',views.follow_up,name='follow_up'),
    url(r'^home_visit/$',views.home_visit,name='home_visit'),
    url(r'^immunization/$',views.immunization,name='immunization'),
    url(r'^sixtothreeyear/$',views.sixtothreeyear,name='sixtothreeyear'),
    url(r'^service/$',views.service,name=''),
    url(r'^zerotosixmonth/$',views.zerotosixmonth,name='zerotosixmonth'),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)