from django.shortcuts import render , get_object_or_404
from .models import Blog , Video 
from .forms import CommentForm , NewsLetterForm
# Create your views here.

def index(request):
    video = Video.objects.all()
    blog = Blog.objects.all()
    if request.method == 'POST':
        newsletter_form = NewsLetterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
    else:
        newsletter_form = NewsLetterForm()
    return render(request,'index.html',{'blog':blog , 'video':video , 'newsletter_form':newsletter_form })

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
    return render(request,'post.html',{'id':id , 'blog':blog , 'comment':comments , 'new_comment': new_comment , 'comment_form': comment_form })