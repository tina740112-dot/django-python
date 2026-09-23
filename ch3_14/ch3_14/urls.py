"""
URL configuration for ch3_14 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set_cookie/<str:key>/<str:value>/', views.set_cookie, name='set_cookie'),
    path('get_cookie/<str:key>/', views.get_cookie, name='get_cookie'),
    path('get_all_cookies/', views.get_all_cookies, name='get_all_cookies'),
    path('set_cookie2/<str:key>/<str:value>/', views.set_cookie2, name='set_cookie2'),
    path('delete_cookie/<str:key>/', views.delete_cookie, name='delete_cookie'),
    path('index/', views.index, name='index'),

    path('set_session/<str:key>/<str:value>/', views.set_session, name='set_session'),
    path('get_session/<str:key>/', views.get_session, name='get_session'),
    path('delete_session/<str:key>/', views.delete_session, name='delete_session'),

    path('vote/', views.vote, name='vote'),
    path('set_session2/<str:key>/<str:value>/', views.set_session2, name='set_session2'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
