from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .yasg_router import urlpatterns as yasg

urlpatterns = [
    path('/api/admin/', admin.site.urls),
    path('/api/jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('/api/jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path("/api/__debug__/", include("debug_toolbar.urls")),

    path('api/v1/', include('src.routers.urls')),
]
urlpatterns += yasg


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
