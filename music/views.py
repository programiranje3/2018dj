from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from music.models import Performer


# def index(request):
#     return HttpResponse("<h1>Hi there :)</h1>")

def index(request):

    n_performers = Performer.objects.all().count()
    rng = range(0, 3)
    context = {
        'num_performers': n_performers,
        'range': rng
    }

    # return render(request, 'index_1.html', context=context)
    return render(request, 'index.html', context=context)


def performer_detail(request, pk):
    # return HttpResponse(str(pk))
    return HttpResponse(str(Performer.objects.get(id=pk).get_absolute_url()))
