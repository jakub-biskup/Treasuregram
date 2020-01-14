from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^([0-9]+)/$', views.detail, name='detail'),
    path('post_url/', views.post_treasure, name='post_treasure'),
    re_path(r'^user/(\w+)/$', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('like_treasure/', views.like_treasure, name='like_treasure')
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    ]
