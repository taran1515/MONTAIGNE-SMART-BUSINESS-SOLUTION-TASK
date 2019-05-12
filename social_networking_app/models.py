from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120)
    author = models.ForeignKey(User,related_name='status_post',on_delete='cascade')
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete='cascade')
    dob = models.DateTimeField(null=True,blank=True)




    def __str__(self):
        return self.user


class Comment(models.Model):

    post = models.ForeignKey(Post,on_delete='cascade',related_name='comments')
    user = models.ForeignKey(User,on_delete='cascade',null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

class Plan(models.Model):
    post = models.ForeignKey(Post, on_delete='cascade', related_name='plans')
    user = models.ForeignKey(User, on_delete='cascade', null=True)
    plan = models.IntegerField(blank=True,null=True)
