from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Subscription_plans, Blog

# Create your views here.

def index(request):
    return render(request, 'index.html')

def features(request):
    return render(request, 'features.html')

def pricing(request):
    plan = Subscription_plans.objects.all().values()
    template = loader.get_template('pricing.html')
    context = {
        'myplan': plan,
    }


    return render(request, 'pricing.html', context)

def buyer(request):
    return render(request, 'solution_buyer.html')

def supplier(request):
    return render(request, 'solution_supplier.html')

def online(request):
    return render(request, 'product_online.html')

def offline(request):
    return render(request, 'product_offline.html')

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def blog(request):
    blog = Blog.objects.all().values()
    template = loader.get_template('blog.html')
    context = {
        'myblog': blog,
    }

    return render(request, 'blog.html', context)
