from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dolphin, Ocean
from .forms import FeedingForm
# Create your views here.

class DolphinCreate(CreateView):
  model = Dolphin
  fields = '__all__'

class DolphinUpdate(UpdateView):
  model = Dolphin
  fields = ['breed', 'description', 'age']

class DolphinDelete(DeleteView):
  model = Dolphin
  success_url = '/dolphins/'

def home(request):
    return HttpResponse('<h1>Hello World</h1>')

def about(request):
    return render(request, 'about.html')

def dolphins_index(request):
  dolphins = Dolphin.objects.all()
  return render(request, 'dolphins/index.html', { 'dolphins': dolphins })

def dolphins_detail(request, dolphin_id):
  dolphin = Dolphin.objects.get(id=dolphin_id)
  oceans_dolphin_doesnt_have = Ocean.objects.exclude(id__in = dolphin.oceans.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'dolphins/detail.html', {
    'dolphin': dolphin, 
    'feeding_form': feeding_form,
    'oceans': oceans_dolphin_doesnt_have
    })

def add_feeding(request, dolphin_id):
  # create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.dolphin_id = dolphin_id
    new_feeding.save()
  return redirect('detail', dolphin_id=dolphin_id)

def assoc_ocean(request, dolphin_id, ocean_id):
  # Note that you can pass a toy's id instead of the whole object
  Dolphin.objects.get(id=dolphin_id).oceans.add(ocean_id)
  return redirect('detail', dolphin_id=dolphin_id)