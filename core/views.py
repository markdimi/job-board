from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer
from .models import Searches

import requests

class JobView(APIView):

    def get_job_data(self, data):
        payload = {'description': data['description'], 'location': data['location']}
        r = requests.get('https://jobs.github.com/positions.json', params=payload)
        return(r.json())
    
    def get(self, request, *args, **kwargs):
        data = {
            'name':"Markos",
            'location' : 'Greece'
        }
        return Response(data)

        # https://jobs.github.com/positions.json?description=python&location=san+francisco

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            job_data = self.get_job_data(serializer.data)
            return Response(job_data)
        return Response(serializer.errors)