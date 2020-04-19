#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from .models import TouristAttraction, Rating
from news.models import News
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string




def Home(request):
    allnews = News.objects.all()
    context = {'allNews': allnews}
    return render(request, 'attraction/home.html', context)


def listAttraction(request):
    attractions_list = TouristAttraction.objects.all()

    query = request.GET.get('q')
    if query:
        attractions_list = attractions_list.filter(
            Q(name__icontains=query)|
            Q(province__icontains=query)|
            Q(address__icontains=query)|
            Q(kindOf__icontains=query)).distinct()
    
    paginator = Paginator(attractions_list, 24) # Show 21 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    

    context = {

        'page_obj': page_obj
        }

    return render(request, 'attraction/attractions.html', context)




def attraction_detail(request, attraction_id):
    detail = get_object_or_404(TouristAttraction, id=attraction_id)
    
    #detail = TouristAttraction.objects.get(id=id)
    context = {
        'detail': detail,
        }
    return render(request, 'attraction/detail.html', context)








def map_view(request):
    return render(request, 'attraction/map.html')