from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages

# List View for Musicians and Albums
class MusicianListView(ListView):
    model = Musician
    template_name = 'musician_list.html'
    context_object_name = 'musicians'

# Create Musician View (LoginRequired)
class MusicianCreateView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'
    success_url = reverse_lazy('musician_list')

# Edit Musician View
class MusicianUpdateView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'
    success_url = reverse_lazy('musician_list')

# Delete Musician View
class MusicianDeleteView( DeleteView):
    model = Musician
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('musician_list')

# Album Create View
class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    success_url = reverse_lazy('musician_list')

# Album Edit View
class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    success_url = reverse_lazy('musician_list')

# Album Delete View
class AlbumDeleteView( DeleteView):
    model = Album
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('musician_list')

def user_logout(request):
    logout(request)
    return redirect('login')