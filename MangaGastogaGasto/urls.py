from django.contrib import admin
from django.urls import path, include
from home.views import home_view
from mangas.views import detail_manga

urlpatterns = [
    path('', home_view),
    path('mangas/', include('mangas.urls')),
    path("admin/", admin.site.urls),
]
