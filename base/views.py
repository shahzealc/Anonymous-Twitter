from asyncio.windows_events import NULL
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from base.models import Tweet
from django.db.models import Q
import datetime
from django.core.files.storage import FileSystemStorage
from newsapi import NewsApiClient

# from . import template

def home(request):

    newsapi = NewsApiClient(api_key ='APIKeywhichicantshowhere')
    top = newsapi.get_top_headlines(sources ='techcrunch')
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
    url =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    news = zip(news, desc, img,url)

    if request.GET.get('tag'):
        q = request.GET.get('tag')
        tweets = Tweet.objects.filter(Q(titlee__icontains=q) | 
                                      Q(description__icontains=q) | 
                                      Q(tag__icontains=q))

    else:
        tweets  = Tweet.objects.all().order_by('-creation_date')

    return render(request,'home.html',{'tweets':tweets,'news':news})

def about(request):
    return render(request,'about.html')

def show_form(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('desc'):
            tweet=Tweet()
            tweet.titlee= request.POST.get('title')
            tweet.description= request.POST.get('desc')
            tweet.tag= request.POST.get('tag')
            # if request.POST.get('image_post'):
            #     tweet.image_post= request.POST.get('image_post')
            tweet.creation_date = datetime.date.today()
            # print(request.FILES['image_post'])
            if request.FILES.get('image_post'):
                image = request.FILES['image_post']
                fs = FileSystemStorage()
                image_name = fs.save(image.name,image)
                url = fs.url(image_name)
                tweet.image_post = url

            tweet.save()


    return render(request,'form.html')
