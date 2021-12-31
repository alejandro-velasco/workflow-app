from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import GitRepos
from .serializer import GitReposSerializer

# Get a list of registered Git repositories
@api_view(['GET'])
def git_repos_list_view(request, *args, **kwargs):
    repo_list = GitRepos.objects.all()
    repos = [x.serialize() for x in repo_list]
    data = {
        "response" : repos
    }
    return Response(data)

# Get Git Repository Details by name
@api_view(['GET'])
def git_repo_detail_by_name_view(request, repo_name, *args, **kwargs):
    data = {
        "name" : repo_name
    }
    status = 200
    try:
        obj = GitRepos.objects.get(name=repo_name)
        data['id'] = obj.id
        data['url'] = obj.url
        data['secure'] = obj.secure
        data['description'] = obj.description
        data['status'] = "ok"

    except:
        data['message'] = "Not Found"
        data['status'] = "error"

    return Response(data, status=status)

# Get Git Repository Details by id
@api_view(['GET'])
def git_repo_detail_by_id_view(request, repo_id, *args, **kwargs):
    data = {
        "id" : repo_id
    }
    status = 200
    try:
        obj = GitRepos.objects.get(id=repo_id)
        data['name'] = obj.name
        data['url'] = obj.url
        data['description'] = obj.description
        data['secure'] = obj.secure
        data['status'] = "ok"

    except:
        data['message'] = "Not Found"
        data['status'] = "error"

    return Response(data, status=status)

# Create Git Repository Entry
@api_view(['POST'])
def git_repo_create_view(request, *args, **kwargs):
    serializer = GitReposSerializer(data=request.data or None)
    if serializer.is_valid(raise_exception = True):
        serializer.save()
        return Response(serializer.data)
    return Response({}, status=400)

# Delete Git repository entry by name
@api_view(['DELETE'])
def git_repo_delete_by_name_view(request, repo_name, *args, **kwargs):
    data = {
        "name" : repo_name
    }
    status = 200
    try:
        obj = GitRepos.objects.get(name=repo_name)
        data['id'] = obj.id
        data['url'] = obj.url
        data['description'] = obj.description
        data['secure'] = obj.secure
        data['status'] = "successfully deleted"
        obj.delete()
    except:
        data['message'] = "Not Found"
        data['status'] = "error"

    return Response(data, status=status)

    # Delete Git repository entry by id
@api_view(['DELETE'])
def git_repo_delete_by_id_view(request, repo_id, *args, **kwargs):
    data = {
        "id" : repo_id
    }
    status = 200
    try:
        obj = GitRepos.objects.get(id=repo_id)
        data['name'] = obj.name
        data['url'] = obj.url
        data['description'] = obj.description
        data['secure'] = obj.secure
        data['status'] = "successfully deleted"
        obj.delete()
    except:
        data['message'] = "Not Found"
        data['status'] = "error"

    return Response(data, status=status)
