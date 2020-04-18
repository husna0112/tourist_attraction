#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from .forms import CreatePlanForm
from .models import News, Plan, TouristAttraction, Rating
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


def listNews(request):
    allnews = News.objects.all()#[:3]


    paginator = Paginator(allnews, 2) # Show 21 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    

    context = {

        'page_obj': page_obj
        }
    return render(request, 'attraction/news.html', context)

def news_detail(request, news_id):
    detail = get_object_or_404(News, id=news_id)
    #detail = TouristAttraction.objects.get(id=id)
    return render(request, 'attraction/news_detail.html', context={'detail': detail})

@login_required
def plan_list_view(request):
    # User = get_user_model()
    # j = User.objects.first()
    qs = Plan.objects.filter(user=request.user).values()

    #allPlans = Plan.objects.all()
    context = {'allPlan': qs}
    return render(request, 'attraction/plan_list.html', context)

@login_required
def plan_detail_view(request, plan_id):
    detail = get_object_or_404(Plan, id=plan_id)
    attractions_list = TouristAttraction.objects.all()
    plan = Plan.objects.get(pk=plan_id)
    attractions = plan.touristattractions.all()
    
    query = request.GET.get('q')
    if query:
        attractions_list = attractions_list.filter(
            Q(name__icontains=query)|
            Q(province__icontains=query)|
            Q(address__icontains=query)|
            Q(kindOf__icontains=query)).distinct()
    
    paginator = Paginator(attractions_list, 5) # Show 21 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {

        'page_obj': page_obj,
        'plan': plan,
        'attractions': attractions,
        'detail': detail,
    }
    
    return render(request, 'attraction/plan_detail.html', context)



@login_required
def plan_create_view(request):
    title = "Create"
    form = CreatePlanForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = CreatePlanForm()
        return redirect('/plan')
    context = {
        'form': form,
        'title': title,
    }
    return render(request, 'attraction/plan_create.html', context)



@login_required
def plan_update_view(request, plan_id):
    obj = get_object_or_404(Plan, id=plan_id)
    form = CreatePlanForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/plan')
    context = {
        'form': form,
        }
    return render(request, 'attraction/plan_update.html', context)

@login_required
def plan_delete_view(request, plan_id):
    obj = get_object_or_404(Plan, id=plan_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/plan')
    success_message = 'Success: Book was deleted.'
    context = {"object": obj}
    return render(request, 'attraction/plan_delete.html', context)





def map_view(request):
    return render(request, 'attraction/map.html')