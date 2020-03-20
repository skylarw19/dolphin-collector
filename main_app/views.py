from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Dolphin:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dolphins = [
  Dolphin('Lolo', 'tabby', 'foul little demon', 3),
  Dolphin('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Dolphin('Raven', 'black tripod', '3 legged cat', 4)
]

def home(request):
    return HttpResponse('<h1>Hello World</h1>')

def about(request):
    return render(request, 'about.html')

def dolphins_index(request):
  return render(request, 'dolphins/index.html', { 'dolphins': dolphins })