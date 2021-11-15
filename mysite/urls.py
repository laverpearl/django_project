"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

"""
from django.contrib import admin
from django.urls import path
from bookmark.views import BookmarkLV, BookmarkDV
from phone.views import PhoneLV, PhoneDV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookmark/', BookmarkLV.as_view(), name='index'),
    path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),
    path('phone/', PhoneLV.as_view(), name='phoneindex'),
    path('phone/<int:pk>/', PhoneDV.as_view(), name='phonedetail'),

]


"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mysite.views import HomeView
from mysite.views import UserCreateView, UserCreateDoneTV

urlpatterns = [
                  path('admin/', admin.site.urls),

                  path('accounts/', include('django.contrib.auth.urls')),
                  path('accounts/register/', UserCreateView.as_view(), name='register'),
                  path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),


                  # shkim
                  path('', HomeView.as_view(), name='home'),
                  path('bookmark/', include('bookmark.urls')),
                  path('phone/', include('phone.urls')),
                  path('blog/', include('blog.urls')),
                  path('namecard/', include('namecard.urls')),
                  path('student/', include('student.urls')),
                  path('photo/', include('photo.urls')),
                  path('gwamok/', include('gwamok.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
