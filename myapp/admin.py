from django.contrib import admin
from myapp.models import Subscription_plans
from myapp.models import Blog

# Register your models here.

class Subscription(admin.ModelAdmin):
    list_display=('plan', 'price', 'validity', 'status','date')
    list_filter = ('status',)
    search_fields = ['plan', 'validity']

admin.site.register(Subscription_plans,Subscription)

class Blogs(admin.ModelAdmin):
    list_display=('title','slug','author','created_on','status')
    list_filter = ('title','author','status',)
    search_fields = ['title','subject']

admin.site.register(Blog,Blogs)
