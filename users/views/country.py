from rest_framework import viewsets

from users.models.country import Country
from users.serializers.country import CountrySerializer


# ViewSets define the view behavior.
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
