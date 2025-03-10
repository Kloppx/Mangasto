from django.urls import path
from mangas.views import detail_manga

urlpatterns = [
    path('mangas/<int:manga_id>/', detail_manga, name='detail_manga'),
]
