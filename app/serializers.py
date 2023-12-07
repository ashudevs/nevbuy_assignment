from rest_framework import serializers
from .models import SumResult

class SumResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SumResult
        fields = ['num1','num2','result']
