from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from blog.models import Post
from django.contrib.auth.models import User

# Create your views here.


def slug_creator(title):
    return "-".join([i.lower() for i in title.split()])


def show_all(request):
    if request.method == 'POST':
        Post.objects.create(title=request.POST['title'], text=request.POST['text'], author=User.objects.get(username='maste'), status="PB", slug=slug_creator(request.POST['title']))
    all_posts = get_list_or_404(Post, status="PB")
    context = {
        "posts": all_posts
    }
    return render(request, "blog/all.html", context)


def show_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Http404()
    context = {
        "post": post
    }
    return render(request, "blog/detail.html", context)


def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        "post": post
    }
    return render(request, "blog/delete.html", context)


def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("blog:show_all")


def change_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.text = request.POST['text']
        post.create_date = post.change_date
        post.save()
        return redirect("blog:show_all")
    context = {
        'post': post
    }
    return render(request, "blog/change.html", context)