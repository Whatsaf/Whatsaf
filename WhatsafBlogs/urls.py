from django.urls import path
from WhatsafBlogs import views

urlpatterns = [
    path("", views.index, name = "BlogPage"),
    path("blogs", views.Blogs, name = "Blogs"),
    path("read-blog/<str:slug>", views.ReadBlog, name = "ReadBlog"),
    path("search", views.Search, name = "Search"),
    path("post-comment", views.PostComment, name = "PostComment"),
    path("like-blog/<int:likeid>", views.LikeBlog, name = "LikeBlog"),
]