"""Tution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from tutor import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.main),
    url(r'^home/$', views.main),
    url(r'^login/$', auth_views.login, {'template_name': 'tutor/login.html'}, name='login'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^register/$', views.user_register),
    url(r'^logout/$', views.logout_page),
    url(r'^accounts/profile/$', views.profile),
    url(r'^userprofile/$', views.manageprofile),
    url(r'^expertise/$', views.add_expertise),
    url(r'^qualifications/$', views.add_qualifications),
    url(r'^addBio/$', views.add_Bio),
    url(r'^tutorDetails/(?P<id>[0-9]+)/$', views.tutorDetails),
    # url(r'^events/(?P<id>[0-9]+)/$', views.event_update),



]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
