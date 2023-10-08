from django.shortcuts import render, get_object_or_404, redirect
from .models import Song

def index(request):
    songs = Song.objects.all()
    return render(request, 'music_app/index.html', {'songs': songs})

def search(request):
    query = request.GET.get('query')
    songs = Song.objects.filter(title__icontains=query) | Song.objects.filter(artist__icontains=query) | Song.objects.filter(year__icontains=query)
    return render(request, 'music_app/search.html', {'songs': songs, 'query': query})

def song_detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, 'music_app/song_detail.html', {'song': song})

def purchase_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    song.is_purchased = True
    song.save()
    return redirect('song_detail', song_id=song_id)

def my_songs(request):
    songs = Song.objects.filter(is_purchased=True)
    return render(request, 'music_app/my_songs.html', {'songs': songs})