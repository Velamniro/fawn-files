from django.contrib import admin
from django.urls import include, path

from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('home.urls')),
    path('file/', include('files.urls')),
    path('user/', include('users.urls')),
    path('nekomu_ne_trogat/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    from django.conf import settings
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
