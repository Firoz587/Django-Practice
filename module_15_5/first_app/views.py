from django.shortcuts import render, redirect, get_object_or_404
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm

def musician_list(request):
    musicians = Musician.objects.all()
    return render(request, 'musician_list.html', {'musicians': musicians})

def musician_create(request):
    form = MusicianForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('musician_list')
    return render(request, 'musician_form.html', {'form': form})

def musician_edit(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    form = MusicianForm(request.POST or None, instance=musician)
    if form.is_valid():
        form.save()
        return redirect('musician_list')
    return render(request, 'musician_form.html', {'form': form})

def musician_delete(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    musician.delete()
    return redirect('musician_list')

def album_create(request):
    form = AlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('musician_list')
    return render(request, 'album_form.html', {'form': form})

def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    form = AlbumForm(request.POST or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect('musician_list')
    return render(request, 'album_form.html', {'form': form})

def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('musician_list')
