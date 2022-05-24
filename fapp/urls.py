from django.urls import path
from django.contrib import admin

urlpattern=[
    path("admin/", admin.site.urls),
]