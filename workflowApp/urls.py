"""workflowApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gitFlow.views import (
    git_repos_list,
    git_repo_detail_by_name,
    git_repo_detail_by_id,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('repos/', git_repos_list, name='git-repo-list'),
    path('repos/name/<str:repo_name>', git_repo_detail_by_name, name='git-repo-name-details'),
    path('repos/id/<int:repo_id>', git_repo_detail_by_id, name='git-repo-id-details'),

]
