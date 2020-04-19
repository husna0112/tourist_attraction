from django.urls import path

from attraction import views

urlpatterns = [
   
   path('', views.listAttraction, name='listAttraction'),
   path('<int:attraction_id>', views.attraction_detail, name='detail'),
   #path(r'^attraction/detail/(?P<attraction_id>\d+)/$', views.attraction_detail, name='detail'),



 
]
