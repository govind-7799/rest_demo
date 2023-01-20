from rest_framework import serializers
from .models import Dummydata


class dummyserilizer(serializers.ModelSerializer):
    class Meta:
        model=Dummydata
        fields='__all__'