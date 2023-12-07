from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SumResultSerializer
from .models import SumResult
from rest_framework import status

@api_view(['POST'])
def sum_numbers(request):
    num1 = int(request.data.get('num1', 0))
    num2 = int(request.data.get('num2', 0))
    result = num1 + num2
    sum_result = SumResult.objects.create(num1=num1, num2=num2, result=result)

    serializer = SumResultSerializer(sum_result)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
