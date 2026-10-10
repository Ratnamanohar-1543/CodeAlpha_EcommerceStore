from django.contrib import admin
from django.urls import path, include
from store import views as v
urlpatterns = [path("admin/", admin.site.urls), path("accounts/register/", v.register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")), path("", include("store.urls"))]
