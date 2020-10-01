from django.shortcuts import render , get_object_or_404,redirect
from .models import Blog , Video ,Author
from .forms import CommentForm , NewsLetterForm , BlogForm
# Create your views here.

def index(request):
    video = Video.objects.all()
    blog = Blog.objects.all()
    author = Author.objects.all()
    if request.method == 'POST':
        newsletter_form = NewsLetterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
    else:
        newsletter_form = NewsLetterForm()
    return render(request,'Pages/index.html',{'blog':blog , 'video':video , 'newsletter_form':newsletter_form , 'author':author })

def post(request,id):
    blog = get_object_or_404(Blog, pk=id)
    comments = blog.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
                # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
                # Assign the current post to the comment
            new_comment.blog = blog
                # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,'Pages/post.html',{'id':id , 'blog':blog , 'comment':comments , 'new_comment': new_comment , 'comment_form': comment_form })

def addpost(request):
    user = request.user
    blog = Blog.objects.all()
    new_post = None
    if request.method == 'POST':
        post_form = BlogForm(data=request.POST)
        if post_form.is_valid():
            new_post = post_form.save()
            new_post.save()
    else:
        post_form = BlogForm()
    return render(request,'Admin/admin.html',{'blog' : blog,'post_form':post_form})

def deletepost(request, id):   
    blog = get_object_or_404(Blog, id = id)   
    if request.method =="POST": 
        blog.delete() 
        return HttpResponseRedirect("/blogadmin")   
    return render(request, "Admin/delete.html",{'blog':blog}) 