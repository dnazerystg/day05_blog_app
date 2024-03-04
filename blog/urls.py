from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.landing_page, name="landing-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.single_post, name="single-post-page"),  # /posts/about-me
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)