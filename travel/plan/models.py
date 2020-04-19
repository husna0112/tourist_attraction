from django.conf import settings
from django.db import models
from django.urls import reverse
from attraction.models import TouristAttraction

class Plan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    detail = models.TextField(null=True, blank=True)
    touristattractions = models.ManyToManyField(TouristAttraction)

    def __str__(self):
        return self.name

  


    def get_plan_url(self):
        return reverse('plan_detail', args=[str(self.id)])

    # def get_edit_url(self):
    #     return f"{self.get_plan_url}/update"

    # def get_delete_url(self):
    #     return f"{self.get_absolute_url}/delete"