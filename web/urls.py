from django.urls import path
from web.views import index,subscribe
from django.conf import settings
from django.conf.urls.static import static


app_name = "web"

urlpatterns = [
    path("",index,name="index"),
    path("subscribe/", subscribe, name="subscribe")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
