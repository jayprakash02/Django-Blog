from django.db import models

# Create your models here.
TAG = [
    ("1", 'Travelling'),
    ("2", 'Food'),
    ("3", 'Technology'),
    ("4", 'Information'),
]
FEATURE = [
    ("1", 'Hot Rated'),
    ("2", 'Most Viewed'),
]


class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    pubDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    title = models.CharField(max_length=50)
    tag = models.CharField(max_length=20, choices=TAG)
    feature = models.CharField(max_length=20, choices=FEATURE)
    blog = models.CharField(max_length=5000)
    desc = models.CharField(max_length=50)
    bg_img = models.ImageField(upload_to='uploads/blog', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['pubDate']
    
class Video(models.Model):
    url = models.URLField( max_length=200)
    title = models.CharField( max_length=50)
    text = models.CharField( max_length=100)
    bg_img = models.ImageField(upload_to='uploads/video', height_field=None, width_field=None, max_length=None)
    pubDate = models.DateTimeField( auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=50, default="Anonymous" , primary_key=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class NewsLetter(models.Model):
    email = models.EmailField(max_length=200 , primary_key=True)
