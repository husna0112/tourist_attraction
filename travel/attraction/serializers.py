from rest_framework import serializers
from .models import TouristAttraction, Rating

class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristAttraction
        fields = ('id', 'name', 'province', 'detail', 'no_of_ratings', 'avg_rating')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'touristattraction')