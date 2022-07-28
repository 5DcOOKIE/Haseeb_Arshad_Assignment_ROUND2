from rest_framework import serializers

from users.models.country import Country
from users.models.city import City
from users.serializers.city import CitySerializer


# Country Serializer
class CountrySerializer(serializers.ModelSerializer):
    # cities = CitySerializer('cities',
    #                         many=True, read_only=True)
    cities = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = ('id', 'name', 'cities')


    def get_cities(self, obj):
        "obj is a Member instance. Returns list of dicts"""
        qset = City.objects.filter(country=obj)
        return [CitySerializer(m).data for m in qset]
