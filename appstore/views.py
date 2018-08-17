from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .forms import PostForm, CommentForm
from .models import Post, Reviews
from django.utils import timezone
from django.views.generic import ListView, DetailView

def reviews (request):
    Reviews = (Reviews.objects.all())
    return render (request, 'reviews_list.html', {'reviews': reviews})

def post_list (request):
    posts = (Post.objects.all())
    return render (request, 'appstore/post_list.html', {'posts': posts})

def post_detail( request, pk):
    post = get_object_or_404(Post,pk=pk)
    #post = DetailView.as_view(model= Post, template_name = 'appstore/post_detail.html')
    return render(request, 'appstore/post_detail.html', {'post': post})
    #<a class="btn btn-default" href="{% url 'post_edit' pk=Post.pk %}"></a>

def post_new(request):
    form_class = PostForm
    form = form_class(request.POST or None)

    if request.method == "POST":
        form=PostForm(request.POST)        
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.update_date = timezone.now()
            post.save()
            return redirect ('post_list')#, pk = Post.pk)
    else:
        form= PostForm()
    return render(request, 'appstore/post_edit.html',{'form': form})
    
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.update_date = timezone.now()
            post.save()
            return redirect('post_list') #pk=Post.pk
    else:
        form = PostForm(instance=post)
    return render(request, 'appstore/post_edit.html', {'form': form})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form_class = CommentForm
    form = form_class(request.POST or None)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_list', pk=Post.pk)
    else:
        form = CommentForm()
    return render(request, 'appstore/add_comment_to_post.html', {'form': form})

def edit_comment_to_post(request, pk):
    post = get_object_or_404(Reviews, pk=pk)
    form_class = CommentForm
    form = CommentForm(request.POST or None)
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance = post)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_list')#, pk=Post.pk)
    else:
        form = CommentForm(instance = post)
    return render(request, 'appstore/add_comment_to_post.html', {'form': form})


