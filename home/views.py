from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Post

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

def home(request):
    recent_posts = Post.objects.order_by("-date")
    recent_posts = recent_posts[:6]
    context = {
        "recent_posts": recent_posts,
    }
    return render(request, "home.html", context)
