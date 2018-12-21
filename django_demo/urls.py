"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from learn import views as learn_views
from rent_proj import views as rent_views

urlpatterns = [
    path('mpa/', include('mpa.urls')),
    path('rent/', rent_views.index),
    path('', learn_views.index),
    path('add/', learn_views.add),
    path('add/<int:a>/<int:b>/', learn_views.add2),
    path('new_add/<int:a>/<int:b>/', learn_views.add2),
    path('admin/', admin.site.urls),
]
