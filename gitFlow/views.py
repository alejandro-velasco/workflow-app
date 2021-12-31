from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import GitRepos

@api_view(['GET'])
def git_repos_list_view(request, *args, **kwargs):
    git_repo_list = GitRepos.objects.all()
    git_repos = [x.serialize() for x in git_repo_list]
    data = {
        "response" : git_repos
    }
    return Response(data)
# Create your views here.
