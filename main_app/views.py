from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dolphin, Ocean
from .forms import FeedingForm
from django.views.generic import ListView, DetailView
# Add the two imports below
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class DolphinCreate(LoginRequiredMixin, CreateView):
  model = Dolphin
  fields = ['name', 'breed', 'description', 'age']
  
  def form_valid(self, form):
    form.instance.user = self.request.user  # form.instance is the cat
    return super().form_valid(form)

class DolphinUpdate(LoginRequiredMixin, UpdateView):
  model = Dolphin
  fields = ['breed', 'description', 'age']

class DolphinDelete(LoginRequiredMixin, DeleteView):
  model = Dolphin
  success_url = '/dolphins/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def dolphins_index(request):
  dolphins = Dolphin.objects.filter(user=request.user)
  return render(request, 'dolphins/index.html', { 'dolphins': dolphins })

@login_required
def dolphins_detail(request, dolphin_id):
  dolphin = Dolphin.objects.get(id=dolphin_id)
  oceans_dolphin_doesnt_have = Ocean.objects.exclude(id__in = dolphin.oceans.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'dolphins/detail.html', {
    'dolphin': dolphin, 
    'feeding_form': feeding_form,
    'oceans': oceans_dolphin_doesnt_have
    })

@login_required
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

@login_required
def assoc_ocean(request, dolphin_id, ocean_id):
  # Note that you can pass a toy's id instead of the whole object
  Dolphin.objects.get(id=dolphin_id).oceans.add(ocean_id)
  return redirect('detail', dolphin_id=dolphin_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
