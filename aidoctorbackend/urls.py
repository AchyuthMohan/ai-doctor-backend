
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),

]
admin.site.site_header  =  "AI Doctor Backend"  
admin.site.site_title  =  "AI Doctor admin site"
admin.site.index_title  =  "AI Doctor Admin Panel"

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)