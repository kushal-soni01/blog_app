from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . forms import PostForm, UserRegisterForm
from django.contrib import messages
from . models import Post

# Create your views here.
def home(request):
    view_mode = request.GET.get('view', 'all')

    if view_mode == 'my':
        if not request.user.is_authenticated:
            messages.error(request, "You need to be logged in to view your posts.")
            return redirect('login')
        posts = Post.objects.filter(author=request.user).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')
        view_mode = 'all'

    return render(request, 'blogapp/home.html', {
        'posts': posts,     
        'view_mode': view_mode,
    })

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blogapp/signup.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blogapp/create_post.html', {
        'form': form,
        'page_title': 'Create a New Post',
        'page_description': 'Share your thoughts, story, or update with your readers.',
        'submit_label': 'Publish Post',
    })


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.author and not request.user.is_superuser:
        messages.error(request, "You are not allowed to edit this post.")
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'blogapp/create_post.html', {
        'form': form,
        'page_title': 'Edit Post',
        'page_description': 'Update your post details and save the changes.',
        'submit_label': 'Save Changes',
    })

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if(request.user != post.author and not request.user.is_superuser):
        messages.error(request, "You are not allowed to delete this post.")
        return redirect('home')
    
    if(request.method == 'POST'):
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('home')
    
    return render(request, 'blogapp/confirm_delete.html', {'post': post})

def post_detail(request, post_id):  
    post = get_object_or_404(Post, id = post_id)
    return render(request, "blogapp/post_detail.html", {"post": post})
