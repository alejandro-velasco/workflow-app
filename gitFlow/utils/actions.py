from git import Repo, InvalidGitRepositoryError, GitCommandError

from django.conf import settings

from rest_framework import status
from rest_framework.response import Response

import os

def repo_setup(repo_url, repo_name, version):
    repo = Repo.clone_from(repo_url, os.path.join(settings.BASE_DIR, "git_repositories", repo_name))
    new_tag = repo.create_tag(version, message='Automatic tag "{0}"'.format(version)) 
    repo.remotes.origin.push(new_tag)
