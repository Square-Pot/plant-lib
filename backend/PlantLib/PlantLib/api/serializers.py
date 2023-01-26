from django.contrib.auth.models import User, Group
from library.models import Plant
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = [
            'uid', 
            'owner',
            'is_deleted',
            'date_created',
            'date_purchase',
            'deta_seeding',
            'genus', 
            'species', 
            'subspecies', 
            'variety', 
            'cultivar', 
            'field_number', 
            'form',
            'affinity',
            'ex',
            'info',
            'geography',
            'source',
            'price',
            'description',
            'user_number',
            'avatar',
        ]