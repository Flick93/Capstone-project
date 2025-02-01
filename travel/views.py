from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination, Comment

def home(request):
    destinations = Destination.objects.all()
    return render(request, 'travel/home.html', {
        'destinations': destinations
    })

def map_view(request):
    destinations = Destination.objects.all()
    return render(request, 'travel/map.html', {
        'destinations': destinations
    })

def destination_detail(request, city):
    destination = get_object_or_404(Destination, city=city)
    return render(request, 'travel/destination_detail.html', {
        'destination': destination
    })

def add_comment(request, city):
   if request.method == 'POST':
       destination = get_object_or_404(Destination, city=city)
       Comment.objects.create(
           destination=destination,
           author=request.user,
           text=request.POST['comment_text']
       )
   return redirect('travel:map')