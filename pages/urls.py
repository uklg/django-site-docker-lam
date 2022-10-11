from django.urls import path, include
from .views import AboutPageView, contactViewD, successViewD, data_flair,baseView,templateView,faqsView, AboutPageView, ServicePageView, ContactPageView, FeedbackPageView, GalleryPageView
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.sitemaps.views import sitemap

from .sitemaps import StaticViewSitemap


sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    #path('', HomePageView.as_view(), name='home'),
    #path('about/', AboutPageView,name='about'),
    path('demolition/', contactViewD,name='demolition'),
    path('dataflair/',data_flair ,name='dataflair'),
    path('base/', baseView, name='base'),
    path('apptemplate/',templateView, name='apptemplate'),
    path('', AboutPageView, name='aboutus'),
    path('services/', ServicePageView, name ='services'),
    path('contact/',ContactPageView, name='contact'),
    path('feedback/',FeedbackPageView,name='feedback'),
    path('gallery/',GalleryPageView,name='gallery'),

 #path('d1/', ,name='d1'),
    #path('dog'), static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    path('faqs/', faqsView, name='faqs' ),
    path('__debug__/', include('debug_toolbar.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')


]
