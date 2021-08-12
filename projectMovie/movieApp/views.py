from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Movie
from . forms import MovieForm
# Create your views here.


def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie': movie})
    # return HttpResponse('this is movie no %s' % movie_id)


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        ratings = request.POST.get('ratings')
        img = request.FILES['img']
        movie = Movie(name=name, desc=desc, year=year, ratings=ratings, img=img)
        movie.save()
        return redirect('/')
    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        # return render(request, 'delete.html', {'movie': movie})
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
