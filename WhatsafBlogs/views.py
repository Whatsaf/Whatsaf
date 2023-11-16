from django.shortcuts import redirect, render
from .models import Blog, BlogComment
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password
from WhatsafPortal.models import UserDetail

# Whatsaf views starts here.
def index(request):
    blogs = Blog.objects.all()
    blog_count = Blog.objects.count()
    blog_counts = blog_count - 1
    blogparams = {
        "blogs" : blogs[Blog.objects.count() - (Blog.objects.count() - 1):Blog.objects.count():-1],
        "item1" : blogs[blog_counts - 0],
        "item2" : blogs[blog_counts - 1],
        "item3" : blogs[blog_counts - 2],
        "blog_counts" : 1,
    }
    return render(request, "WhatsafBlogs/index.html", blogparams)


def Blogs(request):
    blogs = Blog.objects.all()
    return render(request, "WhatsafBlogs/blogs.html", {"blogs" : blogs, "recblogs" : blogs[Blog.objects.count() - (Blog.objects.count() - 1):Blog.objects.count():-1]})

def ReadBlog(request, slug):
    blogs = Blog.objects.get(BlogSlug = slug)
    intblogviews = int(blogs.Views)
    blogs.Views = intblogviews + 1
    blogs.save()
    return render(request, "WhatsafBlogs/read blog.html", {
        "name" : blogs.BlogName, "date" : blogs.BlogDateAdded,
        "desc" : blogs.BlogDescription,
        "image" : blogs.BlogImage,
        "post" : blogs.BlogPost,
        "author" : blogs.BlogAuthor,
        "views" : blogs.Views,
        "likes" : blogs.Likes.count, 
        "allblogs" : (Blog.objects.all())[Blog.objects.count() - (Blog.objects.count() - 1):Blog.objects.count():-1],
        "comments" : BlogComment.objects.filter(BlogDetails=blogs),
        "comments_count" : BlogComment.objects.filter(BlogDetails=blogs).count(),
        "blogid" : blogs.id,
        "views" : blogs.Views,
    })

def PostComment(request):
    if request.method == "POST":
        editPhoto = UserDetail.objects.get(User = User.objects.get(username = request.user.username))
        comment = request.POST["comment"]
        name = request.user.first_name
        blogid = request.POST["id"]
        userdet = User.objects.get(username=request.user)
        blogdet = Blog.objects.get(id = blogid)
        postComment = BlogComment(UserDetails = userdet, Name = name, Email = request.user.email, BlogDetails = blogdet, Comment = comment, User_ProfilePhoto = editPhoto.ProfilePhoto)
        postComment.save()
        messages.success(request, "Your comment has been posted successfully.")
        return redirect(f"/blogs/read-blog/{blogdet.BlogSlug}")
    return redirect("ErrorPage")

def Search(request):
    search_text = request.GET["search"]
    searching = Blog.objects.filter(BlogName__icontains = search_text) or Blog.objects.filter(BlogDescription__icontains = search_text) or Blog.objects.filter(BlogPost__icontains = search_text)
    return render(request, "WhatsafBlogs/search.html", {"searchdata" : searching, "search_text" : search_text, "searchcount" : searching.count(), "blogs" : Blog.objects.all()[Blog.objects.count() - (Blog.objects.count() - 1):Blog.objects.count():-1]})

def LikeBlog(request, likeid):
    blogdet = Blog.objects.get(id=likeid)
    if blogdet.Likes.filter(username = request.user).exists():
        blogdet.Likes.remove(request.user)
        messages.success(request, "Your like has been removed.")
        return redirect(f"/blogs/read-blog/{blogdet.BlogSlug}")
    blogdet.Likes.add(request.user)
    blogdet.save()
    messages.success(request, "Thank you for liking the blog.")
    return redirect(f"/blogs/read-blog/{blogdet.BlogSlug}")
