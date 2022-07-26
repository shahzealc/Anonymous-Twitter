# from multiprocessing import context
# from django.http import HttpResponse
# from django.shortcuts import redirect, render
# from base.models import Tweet
# from django.db.models import Q
# import datetime

# # from . import template

# def home(request):

#     if request.GET.get('tag'):
#         q = request.GET.get('tag')
#         tweets = Tweet.objects.filter(Q(titlee__icontains=q) | 
#                                       Q(description__icontains=q) | 
#                                       Q(tag__icontains=q))

#     else:
#         tweets  = Tweet.objects.all().order_by('-creation_date')

#     return render(request,'home.html',{'tweets':tweets})

# def about(request):
#     return render(request,'about.html')

# def show_form(request):
#     if request.method == 'POST':
#         if request.POST.get('title') and request.POST.get('desc'):
#             tweet=Tweet()
#             tweet.titlee= request.POST.get('title')
#             tweet.description= request.POST.get('desc')
#             tweet.tag= request.POST.get('tag')
#             tweet.image_post= request.POST.get('image_post')
#             tweet.creation_date = datetime.date.today()
#             tweet.save()

#     return render(request,'form.html')