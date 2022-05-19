from django.shortcuts import render
from .models import BlogModel

# Create your views here.

def blogView(request, id):
    article = BlogModel.objects.get(srno=id)
    return render(request, 'blog/article.html', {'article':article})