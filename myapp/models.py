from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Subscription_plans(models.Model):
    class State(models.IntegerChoices):
        INACTIVE = 0
        ACTIVE = 1

    plan = models.CharField(max_length=155)
    price = models.CharField(max_length=255)
    countries = models.CharField(max_length=255)
    validity = models.CharField(max_length=255)
    data_access = models.CharField(max_length=255)
    downloads = models.CharField(max_length=255)
    searches = models.CharField(max_length=255)
    workspace = models.CharField(max_length=255)
    records_ws = models.CharField(max_length=255)
    support = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=State.choices, default=1)


class Blog(models.Model):
    STATUS = (
    (0,"Draft"),
    (1,"Publish"))

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    subject = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog/image')
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title