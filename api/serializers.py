from rest_framework import serializers
from .models import student
class serializerclass(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'

