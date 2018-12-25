from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from music.models import Performer, Song


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


# def performer_detail(request, pk):
#     # return HttpResponse(str(pk))
#     return HttpResponse(str(Performer.objects.get(id=pk).get_absolute_url()))


class PerformerList(ListView):
    model = Performer
    template_name = 'music/performer_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Performer.objects.all()


class PerformerDetail(DetailView):
    model = Performer


class PerformerCreate(CreateView):
    model = Performer
    fields = '__all__'


class PerformerUpdate(UpdateView):
    model = Performer
    fields = ['name', 'is_band']


class PerformerDelete(DeleteView):
    model = Performer
    success_url = reverse_lazy('performer-list')


class SongList(ListView):
    model = Song
    template_name = 'music/song_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Song.objects.all()


class SongDetail(DetailView):
    model = Song


class SongCreate(CreateView):
    model = Song
    fields = '__all__'


class SongUpdate(UpdateView):
    model = Song
    fields = ['title', 'performer', 'time', 'release_date']


class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('song-list')


