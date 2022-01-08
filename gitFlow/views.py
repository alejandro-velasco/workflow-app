from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import GitRepos
from .serializer import GitReposSerializer
from .utils.actions import repo_setup, repo_delete, repo_update

@api_view(['GET', 'POST'])
def git_repos_list(request, *args, **kwargs):
    """
    GET: lists all current repositories
    POST: Creates a new repository entry
    """
    if request.method == 'GET':
        git_repos = GitRepos.objects.all()
        serializer = GitReposSerializer(git_repos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GitReposSerializer(data=request.data)
        if serializer.is_valid():
            try:
                repo_setup(serializer.validated_data)
            except Exception as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get Git Repository Details by name
@api_view(['GET', 'PUT', 'DELETE'])
def git_repo_detail(request, repo_name, *args, **kwargs):
    """
    GET: Gets Repository Specified by name
    PUT: Updates Repository Specified by name
    DELETE: Deletes Repository Specified by name
    """
    try:
        obj = GitRepos.objects.get(name=repo_name)
    except GitRepos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GitReposSerializer(obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GitReposSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                repo_update(serializer.validated_data, repo_name)
            except ValueError as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)   
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            repo_delete(getattr(obj, 'name'))
            obj.delete()
        except FileNotFoundError:
            obj.delete()
            return Response('File Was Not Found. Deleted Reference to maintain database integrity.',
                            status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
