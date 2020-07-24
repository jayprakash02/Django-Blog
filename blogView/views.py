from django.shortcuts import render
from .models import Blog , Video
# Create your views here.

def index(request):
    video = Video.objects.all()
    blog = Blog.objects.all()
    return render(request,'index.html',{'blog':blog , 'video':video })

def post(request,id):
    blog = Blog.objects.all()
    return render(request,'post.html',{'id':id ,'blog':blog })