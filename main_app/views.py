from django.shortcuts import render

musicians = [
  {'name': 'Thom Yorke', 'age': '54', 'role': 'vocalist, songwriter', 'description': 'The main vocalist and songwriter of the rock band Radiohead.'},
  {'name': 'Kevin Parker', 'age': '37', 'role': 'songwriter, multi-instrumentalist', 'description': 'An Australian singer, songwriter, multi-instrumentalist, musician, record producer, and DJ, best known for his musical project Tame Impala.'},
  {'name': 'Lana Del Rey', 'age': '38', 'role': 'singer/songwriter', 'description': 'an American singer-songwriter. Her music is noted for its cinematic quality and exploration of tragic romance, glamour, and melancholia, with frequent references to contemporary pop culture and 1950s–1970s Americana.'},
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def musicians_index(request):
    return render(request, 'musicians/index.html', {
        'musicians': musicians
    })
