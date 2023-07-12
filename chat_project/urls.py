from django.urls import include, path, re_path
from rest_framework import routers
from chat import views
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi
from django.contrib import admin


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]


