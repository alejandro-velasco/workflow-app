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
    git_repos_list_view,
    git_repo_detail_by_name_view,
    git_repo_delete_by_name_view,
    git_repo_detail_by_id_view,
    git_repo_delete_by_id_view,
    git_repo_create_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('repos/', git_repos_list_view),
    path('repos/name/<str:repo_name>', git_repo_detail_by_name_view),
    path('repos/id/<int:repo_id>', git_repo_detail_by_id_view),
    path('repos/create', git_repo_create_view),
    #path('repos/update', git_repo_create_update_view),
    path('repos/delete/name/<str:repo_name>', git_repo_delete_by_name_view),
    path('repos/delete/id/<str:repo_id>', git_repo_delete_by_id_view),

]
