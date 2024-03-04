from django.shortcuts import render
from datetime import date
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.

all_posts = [
    {
        "slug": "smoothie-recipe",
        "image": "ss.png",
        "title": "thing1",
        "author": "Jiminy",
        "date": date(2024, 2, 20),
        "summary": "Gobble gobble",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Quaerat, labore aut commodi ea unde aliquam nisi quisquam consectetur, 
            molestiae, ducimus laboriosam ab incidunt! Accusamus odio nulla, laudantium velit temporibus atque!
        """
    },
    {
        "slug": "butter-recipe",
        "image": "ss.png",
        "title": "thing2",
        "author": "Jiminy",
        "date": date(2024, 1, 20),
        "summary": "Have mercy",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Quaerat, labore aut commodi ea unde aliquam nisi quisquam consectetur, 
            molestiae, ducimus laboriosam ab incidunt! Accusamus odio nulla, laudantium velit temporibus atque!
        """
    },
    {
        "slug": "rock-recipe",
        "image": "ss.png",
        "title": "thing3",
        "author": "Jiminy",
        "date": date(2024, 3, 20),
        "summary": "Geodude",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Quaerat, labore aut commodi ea unde aliquam nisi quisquam consectetur, 
            molestiae, ducimus laboriosam ab incidunt! Accusamus odio nulla, laudantium velit temporibus atque!
        """
    }
]


def get_date(post):
    return post['date']


def landing_page(request):
    latest_posts = Post.objects.all().order_by("-date")[2:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def single_post(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})

# def landing_page(request):
#     sorted_posts = sorted(all_posts, key=get_date)
#     latest_posts = sorted_posts[-2:]
#     return render(request, "blog/index.html", {"posts": latest_posts})


# def posts(request):
#     return render(request, "blog/all-posts.html", {"all_posts": all_posts})


# def single_post(request, slug):
#     identified_post = next(post for post in all_posts if post['slug'] == slug)
#     return render(request, "blog/post-detail.html", {"post": identified_post})