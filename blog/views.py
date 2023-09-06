from django.shortcuts import render
from django.views.generic import DetailView,TemplateView,ListView

from .models import BlogPost

def announcements(request):
    latest_post= BlogPost.objects.all().filter(latest=True)
    posts = BlogPost.objects.all().filter(post_type="announcement").exclude(latest=True)
    return render(request,template_name="main.html",context={"posts":posts,"latest_post":latest_post})

class PostDetailView(DetailView):
    model= BlogPost
    context_object_name="post"
    template_name="post_detail.html"
    
class SoonTemplateView(TemplateView):
    template_name="soon.html"
class AboutTemplateView(TemplateView):
    template_name="about.html"

class GamesListView(ListView):
    model=BlogPost
    context_object_name="projects"
    template_name="games.html"