from blog.choices import RELEVANCE_CHOICES
from .forms import PostForm
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post

RELEVANCE_CHOICES_DICT = {}
for i in RELEVANCE_CHOICES:
    RELEVANCE_CHOICES_DICT[i[0]] = i[1]

def translate_RELEVANCE_CHOICES(Object):
    flag = False
    try:
        iter(Object)
    except:
        flag = True
        Object = [Object]
    for i, _ in enumerate(Object):
        Object[i].relevance = RELEVANCE_CHOICES_DICT[Object[i].relevance]
    if flag:
        return Object[0]
    return Object

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = translate_RELEVANCE_CHOICES(posts)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post = translate_RELEVANCE_CHOICES(post)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.relevance = request.relevance
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.relevance = request.relevance
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})