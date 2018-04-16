from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse
# Create your views here.

from django.utils import timezone


def index(request):
    return render(request, 'index.html')
def more(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'more.html', {'posts': posts})

