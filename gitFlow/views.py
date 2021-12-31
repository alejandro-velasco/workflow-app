from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import GitRepos
from .serializer import GitReposSerializer

# Get a list of registered Git repositories
@api_view(['GET', 'POST'])
def git_repos_list(request, *args, **kwargs):
    if request.method == 'GET':
        git_repos = GitRepos.objects.all()
        serializer = GitReposSerializer(git_repos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GitReposSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get Git Repository Details by name
@api_view(['GET', 'PUT', 'DELETE'])
def git_repo_detail_by_name(request, repo_name, *args, **kwargs):
    try:
        obj = GitRepos.objects.get(name=repo_name)
    except GitRepos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GitReposSerializer(obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GitReposSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Get Git Repository Details by id
@api_view(['GET', 'PUT', 'DELETE'])
def git_repo_detail_by_id(request, repo_id, *args, **kwargs):
    try:
        obj = GitRepos.objects.get(id=repo_id)
    except GitRepos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GitReposSerializer(obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GitReposSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
