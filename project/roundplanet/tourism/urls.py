from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('packages',views.packages,name='package'),
    path('news',views.news,name='news'),
    path('gallery',views.gallery,name='gallery'),
    path('contact',views.contact,name='contact'),
    path('subpack/<int:id>/',views.Subpackages,name='subpack'),
    path('testimonials',views.test,name='testimonials'),
    path('event',views.event,name='event'),
   
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)