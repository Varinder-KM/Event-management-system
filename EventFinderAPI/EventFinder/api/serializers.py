from rest_framework import serializers
from EventFinder.models import Event

class EventSerializer(serializers.Serializer):
    event_id = serializers.IntegerField(read_only=True)
    event_name = serializers.CharField(max_length=200)
    city = serializers.CharField(max_length=200)
    date = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y', 'iso-8601'])
    time = serializers.TimeField(format="%H-%M-%S", input_formats=["%H-%M-%S", 'iso-8601'])
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

    def create(self, validated_data):
        return Event.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.event_id = validated_data.get('event_id', instance.event_id)
        instance.event_name = validated_data.get('event_name', instance.event_name)
        instance.city = validated_data.get('city', instance.city)
        instance.date = validated_data.get('date', instance.date)
        instance.time = validated_data.get('time', instance.time)
        instance.langitude = validated_data.get('latitude', instance.langitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)

        return instance