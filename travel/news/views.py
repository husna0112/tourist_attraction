from django.shortcuts import render, get_object_or_404
from .models import News
from django.core.paginator import Paginator

def listNews(request):
    allnews = News.objects.all()#[:3]
    paginator = Paginator(allnews, 2) # Show 21 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj
        }
    return render(request, 'news/news.html', context)

def news_detail(request, news_id):
    detail = get_object_or_404(News, id=news_id)
    #detail = TouristAttraction.objects.get(id=id)
    return render(request, 'news/news_detail.html', context={'detail': detail})