from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('users/', include('apps.users.urls')),
        path('projects/', include('apps.projects.urls')),
        path('payments/', include('apps.payments.urls')),
        path('blog/', include('apps.blog.urls')),
        path('support/', include('apps.support.urls')),
        path('analytics/', include('apps.analytics.urls')),
        path('surveys/', include('apps.surveys.urls')),
        path('testimonials/', include('apps.testimonials.urls')),
        path('partner/', include('apps.api.urls')),
    ])),

    # API Schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
