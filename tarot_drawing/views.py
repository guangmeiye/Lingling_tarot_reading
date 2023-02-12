from django.shortcuts import render

# Create your views here.
def tarot_drawing(request):
    return render(request, 'tarot_drawing.html', {})