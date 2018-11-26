# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from imdb_videos.models import Videos
from imdb_videos.serializers import VideosSerializer

@csrf_exempt
def all_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Videos.objects.all()
        serializer = VideosSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VideosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def all_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        videos = Videos.objects.get(pk=pk)
    except Videos.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VideosSerializer(videos)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VideosSerializer(videos, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        videos.delete()
        return HttpResponse(status=204)
