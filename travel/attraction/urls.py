from django.urls import path

from attraction import views

urlpatterns = [
   
   path('attraction/', views.listAttraction, name='listAttraction'),
   path('attraction/<int:attraction_id>', views.attraction_detail, name='detail'),
   #path(r'^attraction/detail/(?P<attraction_id>\d+)/$', views.attraction_detail, name='detail'),
   path('news/', views.listNews, name='listNews'),
   path('news/<int:news_id>/', views.news_detail, name='news_detail'),
   path('plan/', views.plan_list_view, name='listPlan'),
   path('plan/<int:plan_id>/', views.plan_detail_view, name="plan_detail"),

   path('plan/<int:plan_id>/edit/', views.plan_update_view, name="plan_update"),
   path('plan/<int:plan_id>/delete/', views.plan_delete_view, name="plan_delete"),
   path('plan/new/', views.plan_create_view, name="plan_create"),
   path('map/', views.map_view, name="map"),


 
]
