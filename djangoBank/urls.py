from django.urls import path
from django.urls import include
from django.contrib import admin


urlpatterns = [

    path("", include("money.urls")),
    path("admin/", admin.site.urls),

]