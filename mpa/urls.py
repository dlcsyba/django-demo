from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from mpa.user.UserView import UserViewSet

router = DefaultRouter()
router.register('user', UserViewSet)

app_name = 'mpa'

urlpatterns = [
    path('', views.home, name='home1'),
    path('home/', views.home, name='home'),
    path('demos/<str:a>/<str:b>', views.demos, name='demo'),
    # path('elements/<str:a>/', mpam_views.elements),
    # path('components/<str:a>/', mpam_views.components),
    # path('tables/<str:a>/', mpam_views.tables),
    # path('charts/<str:a>/', mpam_views.charts),
    #path('to_register/', views.to_register, name='to_register'),
    #path('to_reset_pw/', views.to_reset_pw, name='to_reset_pw'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('reset_pw/', views.reset_pw, name='reset_pw'),
    path('index/', views.index, name='index')
]
