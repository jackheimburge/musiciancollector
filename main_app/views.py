from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Band, Award
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
    id_list = band.awards.all().values_list('id')
    awards_band_doesnt_have = Award.objects.exclude(id__in=id_list)

    musician_form = MusicianForm()
    return render(request, 'bands/detail.html', {
        'band': band,
        'musician_form': musician_form ,
        'awards': awards_band_doesnt_have                                      
        })

class BandCreate(CreateView):
    model = Band
    fields = ['name', 'genre', 'description']

class BandUpdate(UpdateView):
    model = Band
    fields = ['name', 'genre', 'description']

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

class AwardList(ListView):
    model = Award

class AwardDetail(DetailView):
    model = Award

class AwardUpdate(UpdateView):
    model = Award
    fields = '__all__'

class AwardDelete(DeleteView):
    model = Award
    success_url = '/awards'

class AwardCreate(CreateView):
    model = Award
    fields = '__all__'

def assoc_award(request, band_id, award_id):
    Band.objects.get(id=band_id).awards.add(award_id)
    return redirect('detail', band_id=band_id)

def unassoc_award(request, band_id, award_id):
    Band.objects.get(id=band_id).awards.remove(award_id)
    return redirect('detail', band_id=band_id)