"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# include는 그 다음 url경로로 연결시켜줌
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # articles로 시작되는 url로 접속이 들어오면 나머지는 include후의 url너가 알아서해
    path('articles/', include('articles.urls')),
]
