from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from post.models import Post
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic.edit import DeleteView, UpdateView


# Create your views here.


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def home(request):
    post = Post.objects.all()
    return render(request, 'post_list.html', {'Posts': post})


def hello(request):
    return render(request, "hello.html")


def greet(request):
    return HttpResponse("welcome to django")


def greeting(request):
    return render(request, "index.html")


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = {'title', 'body', 'author'}


class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = {'title', 'body'}
