from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Band
from .forms import MusicianForm



# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bands_index(request):
    return render(request, 'bands/index.html', {
        'bands': Band.objects.all()
    })

def bands_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    musician_form = MusicianForm()
    return render(request, 'bands/detail.html', {
        'band': band,
        'musician_form': musician_form                                       
        })

class BandCreate(CreateView):
    model = Band
    fields = '__all__'

class BandUpdate(UpdateView):
    model = Band
    fields = '__all__'

class BandDelete(DeleteView):
    model = Band
    success_url = '/bands'

def add_musician(request, band_id):
    form = MusicianForm(request.POST)
    if form.is_valid():
        new_musician = form.save(commit=False)
        new_musician.band_id = band_id
        new_musician.save()
    return redirect('detail', band_id=band_id)

