from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "weekly" # تغيير أسبوعي أفضل للمواقع النشطة
    protocol = 'https'  # تأكد من تفعيل SSL على السيرفر

    def items(self):
        return [
            'home:home',
            'about:about',
            'catalog:catalog',
            'contact:send_text'
        ]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        if item == 'home:home':
            return 1.0
        elif item == 'catalog:catalog':
            return 0.8
        else:
            return 0.5

    def changefreq(self, item):
        if item == 'home:home':
            return 'daily'
        elif item == 'catalog:catalog':
            return 'weekly'
        else:
            return 'monthly'