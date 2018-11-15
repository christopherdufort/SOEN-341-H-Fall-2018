"""library URL Configuration

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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Catalogue

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign-in', views.sign_in),
    path('book-entry', views.book_entry),
    path('create-account', views.create_account),
    path('client-home', views.client_home),
    path('magazine-entry', views.magazine_entry),
    path('video-entry', views.video_entry),
    path('register-admin', views.register_admin),
    path('catalogue', Catalogue.as_view()),
    path(r'^$', views.homepage),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)