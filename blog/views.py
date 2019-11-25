from django.http import HttpResponse
from django.utils import timezone
from blog.models import Post, Comment

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import PostForm, CommentForm

import json


def main(request):
    return render(request, 'main.html', {})


def about(request):
    return render(request, 'about.html', {})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()

    # post comment
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'form': form})


@login_required
def post_add(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'post_edit.html', {'form': form})


@login_required
def post_delete(request, pk):
    # post = get_object_or_404(Post, pk=pk)
    post = Post.objects.get(id=pk)
    post.delete()

    return redirect('post_list')


def comment_like(request):
    if request.method == 'POST':
        comment_id = request.POST.get('pk', None)
        comment = Comment.objects.get(id=comment_id)

        if not request.user.is_authenticated:
            context = {'like_count': comment.like.count(), 'success': 'authRequired'}
        else:
            user = request.user.id

            if comment.like.filter(id=user).exists():
                comment.like.remove(user)
                message = 'rem'
            else:
                comment.like.add(user)
                message = 'add'

            context = {'like_count': comment.like.count(), 'success': message}

        return HttpResponse(json.dumps(context), content_type='application/json')
