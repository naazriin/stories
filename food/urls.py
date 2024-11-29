"""
URL configuration for food project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from accounts.views import activate


urlpatterns = [
    path("admin/", admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('api/', include('recipes.api.urls')),
    path('auth/', include('accounts.api.urls')),

    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
        activate, name='activate'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += i18n_patterns(
    path('i18n/', include("django.conf.urls.i18n")),
    path("", include("core.urls")),
    path("recipes/", include("recipes.urls")),
    path("accounts/", include("accounts.urls")),
    path("blogs/", include("blogs.urls")),
    path('social-auth/', include('social_django.urls', namespace='social')),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)











