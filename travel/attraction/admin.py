
from django.contrib.auth.models import Permission
from django.contrib import admin

from .models import TouristAttraction, News, Rank, Plan, Rating


admin.site.register(Permission)


class TouristAttractionAdmin(admin.ModelAdmin):
    list_display = ['name','province','kindOf']
    list_per_page = 20

    list_filter = ['province']
    search_fields = ['name']

admin.site.register(TouristAttraction, TouristAttractionAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'detail', 'updated', 'timestamp']
    list_per_page = 20

    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'detail']
admin.site.register(News, NewsAdmin)

class RankAdmin(admin.ModelAdmin):
    list_display = ['rank_number', 'rank_type', 'touristattraction_id']
    list_per_page = 20

    list_filter = ['rank_type']
    #search_fields = ['title']
admin.site.register(Rank, RankAdmin)

admin.site.register(Plan)
admin.site.register(Rating)