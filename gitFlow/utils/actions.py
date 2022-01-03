from git import Repo, InvalidGitRepositoryError, GitCommandError

from rest_framework import status
from rest_framework.response import Response

import os

def repo_setup(repo_url, repo_name, version):
    """
    Clones and tags repository referenced in the POST for /repos
    """
    repo = Repo.clone_from(repo_url, os.path.join(os.environ.get('GIT_REPOSITORY_PATH'), repo_name))
    new_tag = repo.create_tag(version, message='Automatic tag "{0}"'.format(version))
    repo.remotes.origin.push(new_tag)

def repo_delete(repo_name):
    """
    Deletes repository from git repositories path
    """
    os.remove(os.path.join(os.environ.get('GIT_REPOSITORY_PATH'), repo_name))
