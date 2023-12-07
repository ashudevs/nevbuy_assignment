from django.urls import path
from .views import sum_numbers

urlpatterns = [
    path('sum/', sum_numbers, name='sum_numbers'),
]
