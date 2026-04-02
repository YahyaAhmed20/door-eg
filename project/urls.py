"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

# ✅ 1. Imports for Sitemap and Robots
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap  # تأكد أن مسار الاستيراد صحيح حسب مكان ملف sitemaps.py
from home.views import robots_txt  # تأكد أن مسار الاستيراد صحيح حسب مكان دالة robots_txt

# ✅ 2. Define Sitemaps Dictionary
sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # App URLs
    path('', include('home.urls', namespace='home')),
    path('about/', include('about.urls', namespace='about')),
    path('services/', include('services.urls', namespace='services')),
    path('contact-us/', include('contact.urls', namespace='contact')),
    path('catalog/', include('catalog.urls', namespace='catalog')),

    # ✅ 3. SEO URLs (Sitemap & Robots)
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt, name='robots'),
]

# Static and Media files handling for Debug mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)