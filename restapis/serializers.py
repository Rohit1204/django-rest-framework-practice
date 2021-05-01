from rest_framework import serializers

from .models import Hero

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias')


#serialization is the process of converting a Model to JSON. Using a serializer, we can specify what fields should be present in the JSON representation of the model.
# The serializer will turn our heroes into a JSON representation so the API user can parse them, even if they’re not using Python. In turn, when a user POSTs JSON data to our API, the serializer will convert that JSON to a Hero model for us to save or validate.