from django.shortcuts import render

musicians = [
  {'name': 'Thom Yorke', 'age': '54', 'role': 'vocalist, songwriter', 'description': 'The main vocalist and songwriter of the rock band Radiohead.'},
  {'name': 'Kevin Parker', 'age': '31', 'role': 'songwriter, multi-instrumentalist', 'description': 'An Australian singer, songwriter, multi-instrumentalist, musician, record producer, and DJ, best known for his musical project Tame Impala.'},
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
