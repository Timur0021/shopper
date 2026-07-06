from django.shortcuts import render
from .models import Category

# Create your views here.
def index(request):
    categories = Category.objects.filter(active=True).order_by('id')
    return render(request, 'main/index.html', {'title': 'Головна сторінка', 'categories': categories})

def about(request):
    return render(request, 'main/about.html')