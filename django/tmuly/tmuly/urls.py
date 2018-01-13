"""tmuly URL Configuration

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
from pokyu import views as pokyu_views  # new

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', pokyu_views.hello),
    url(r'^test2/', pokyu_views.test, name='test'),

    url(r'^$',pokyu_views.index, name='index'), #blog`s index
    url(r'^index/',pokyu_views.index, name='index'),
    url(r'^about/',pokyu_views.about, name='about'),
    url(r'^services/',pokyu_views.services, name='services'),
    url(r'^contact/',pokyu_views.contact, name='contact'),

    # Portfolio
    url(r'^portfolio-1-col/',pokyu_views.portfolio_1_col, name='portfolio-1-col'),

    # Other Pages
    url(r'^full-width/',pokyu_views.full_width, name='full-width'),
    url(r'^sidebar/',pokyu_views.sidebar, name='sidebar'),
    url(r'^faq/',pokyu_views.faq, name='faq'),
    url(r'^404/',pokyu_views.pokyu404, name='404'),
    url(r'^pricing/',pokyu_views.pricing, name='pricing'),
]

