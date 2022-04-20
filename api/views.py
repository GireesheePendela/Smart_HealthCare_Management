from django.shortcuts import render
from rest_framework import viewsets
from . models import Disease
from api.serializers import DiseaseSerializer
from . import diseaseml
from rest_framework.response import Response
from django.contrib.auth.models import User


class DiseaseViewSet(viewsets.ModelViewSet):
    queryset=Disease.objects.all().order_by('-id')
    serializer_class=DiseaseSerializer
    def create(self, request, *args,**kwargs):
          super(viewsets.ModelViewSet, self).create(request,*args,**kwargs)
          ob=Disease.objects.latest('id')
          sur=diseaseml.pred(ob)
          return Response({"status":"Success","Disease":sur,'tmp':args})
          

         
