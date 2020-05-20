"""try_dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path,include
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

from .views import (home_page,
                    about_page,
                    contact_page,
                    example_page,
                    )
from blogx.views import (
                         blog_post_create_view,
)
from blogx import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^contacts?/$', contact_page),
    re_path(r'^about ?u?s?/$', about_page),
    re_path(r'^homepage?/$', home_page),
    re_path(r'^example?/$', example_page),
    path('', home_page),
    path('blog-new/', blog_post_create_view),
    path('blog/',include('blogx.urls'))

]
