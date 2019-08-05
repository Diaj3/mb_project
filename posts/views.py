from django.shortcuts import render
from django.views.generic import ListView #returns an obj calles object_list that we are gonna display in our template
from .models import Post #What model we are using in the View

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'