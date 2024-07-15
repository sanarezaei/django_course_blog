# from django.shortcuts import render, redirect
from .models import Post
# from django.core.exceptions import ObjectDoesNotExist
# from django.shortcuts import get_object_or_404
# from django.contrib.auth.models import User
from .forms import PostForm
from django.views import generic
from django.urls import reverse_lazy

# def post_list_view(request):
#     posts_list = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/posts_list.html', {'posts_list': posts_list})

class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'
    
    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')
    

# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html' 
    context_object_name = 'post'


# def post_create_view(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = PostForm()
#             return redirect('posts_list')

#     else:
#         form = PostForm()
#     return render(request, 'blog/post_create.html', context={'form': form})
        
    # if request.method == 'POST':
    #     post_title = request.POST.get('title')
    #     post_text = request.POST.get('text')
        
    #     user = User.objects.all()[0]
        
    #     Post.objects.create(title=post_title, text=post_text, author=user, status='pub')
    # else:
    #     print('get request')
    # return render(request, 'blog/post_create.html')

class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'


# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('posts_list')
#     return render(request, 'blog/post_create.html', context={"form": form})

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    


# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         post.save()
#         return redirect('posts_list')
    
#     return render(request, 'blog/post_delete.html', context={'post': post}) 


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')
    
    