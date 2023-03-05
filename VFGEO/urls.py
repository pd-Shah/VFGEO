from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from django.urls import path, include, re_path
import debug_toolbar
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

# from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    re_path(r"^__debug__/", include(debug_toolbar.urls)),
    # swagger Schema routes, Display all APIs
    path("v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
