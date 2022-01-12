
from django.contrib import admin
from django.urls import path,include
from Accounts import views as v
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.index),
    path("Acc",include(("Accounts.urls",'Accounts'),namespace='Accounts')),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
