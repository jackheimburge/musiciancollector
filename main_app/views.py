from django.shortcuts import render

bands = [
  {'name': 'Radiohead', 'genre': 'Experimental Rock', 'formed': '1985', 'description': 'Radiohead is an English rock band formed in Abingdon, Oxfordshire, in 1985. The band consists of Thom Yorke (vocals, guitar, piano, keyboards); the brothers Jonny Greenwood (guitar, keyboards, other instruments) and Colin Greenwood (bass); Ed O Brien (guitar, backing vocals); and Philip Selway (drums, percussion).'},
  {'name': 'Tame Impala', 'genre': 'Psychedelic Pop', 'formed': '2007', 'description': 'Tame Impala is the psychedelic music project of Australian multi-instrumentalist Kevin Parker. In the recording studio, Parker writes, records, performs, and produces all of Tame Impala music. As a touring act, Tame Impala consists of Parker (vocals, guitar, synthesizer), Dominic Simper (guitar, synthesiser), Jay Watson (synthesiser, vocals, guitar), Cam Avery (bass guitar, vocals, synthesizer), and Julien Barbagallo (drums, vocals).'},
  {'name': 'Grizzly Bear', 'genre': 'Art Rock', 'formed': '2002', 'description': 'Grizzly Bear is an American rock band from Brooklyn, New York, formed in 2002. For most of its tenure, the band has consisted of Edward Droste (vocals, keyboards, guitar), Daniel Rossen (vocals, guitar, banjo, keyboards), Chris Taylor (bass, backing vocals, woodwinds, production), and Christopher Bear (drums, percussion, backing vocals).'},
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def musicians_index(request):
    return render(request, 'musicians/index.html', {
        'bands': bands
    })
