"""videoanalyticsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static

from video_analytics_app import views
from videoanalyticsproject import settings

urlpatterns = [
    path('demo', views.showDemoPage),
    path('admin/', admin.site.urls),
    path('',views.ShowLoginPage),
    path('login_user/',views.LoginUser,name='login_user'),
    path('doLogin',views.doLogin),
    path('homepage/',views.HomePage, name="homepage"),
    path('logout/',views.LogoutUser,name='logout'),
    path('addData',views.addData,name="add_data"),
    path('add_video',views.AddVideo, name="add_video"),
    path('view_video',views.ViewVideo, name="view_video"),
    path('videochart',views.VideoChart, name="videochart"),
    path('add_video_analytics',views.AddVideoAnalytics, name="add_video_analytics"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
