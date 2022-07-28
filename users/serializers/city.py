from rest_framework import serializers

from users.models.city import City


# City Serializer
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'country')
