from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('song/<int:song_id>/', views.song_detail, name='song_detail'),
    path('purchase/<int:song_id>/', views.purchase_song, name='purchase_song'),
    path('my_songs/', views.my_songs, name='my_songs'),
]