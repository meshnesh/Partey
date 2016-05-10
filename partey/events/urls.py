from django.conf.urls import include, url

import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^event/type/([^/]+)/$', views.event_type, name='events'),
    url(r'^events/', include('swingtime.urls')),
    ]