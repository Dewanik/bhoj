from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AdPage, CateringCategory
from .serializers import AdPageSerializer,CateringCategorySerializer
# Create your views here.
def test(req):
    return render(req,"home.html")



class AdPageListView(APIView):
    def get(self, request, *args, **kwargs):
        adpages = AdPage.objects.filter(status='p')  # Only fetch published ads
        serializer = AdPageSerializer(adpages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class CateringCategoriesListView(APIView):
    def get(self, request, *args, **kwargs):
        categories = CateringCategory.objects # Only fetch published ads
        serializer = CateringCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
def caterers(req):
    return render(req,"cater.html")