from rest_framework import viewsets

from users.models.city import City
from users.serializers.city import CitySerializer


# ViewSets define the view behavior.
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
