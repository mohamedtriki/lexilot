"""lexilot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings
from users import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name='home'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',views.home,name="landing"),
    path('category/',views.category,name="category"),
    path('category/photographer/',views.photographer,name="photographer"),
    path('category/designer/',views.designer,name="designer"),
    path('category/artist/',views.artist,name="artist"),
    path('category/illustrator/',views.illustrator,name="illustrator"),
    path('category/makeup/',views.makeup,name="makeup"),
    path('category/makeup/edit',views.edit,name="edit"),
    path('success/', views.success_view, name='payments-success'),   # only for the Coinbase charges approach
    path('cancel/', views.cancel_view, name='payments-cancel'),      # only for the Coinbase charges approach
    path('user/',views.user,name="profile"),
    path('logout_user/', views.logout_user ,name='logout_user'),


]
urlpatterns+= staticfiles_urlpatterns()          
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)