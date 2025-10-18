from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from AsiaTourAgency.models import Tour
tours = Tour.objects.all()
context = {'tours': tours}
def index(request):
  return render(request, 'tours/index.html', context)

