from rest_framework import serializers
from .models import Human

class HumanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Human
        fields = ('name', 'address', )

