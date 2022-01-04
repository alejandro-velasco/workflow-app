from git import Repo, InvalidGitRepositoryError, GitCommandError

from rest_framework import status
from rest_framework.response import Response
from .cryptography import decrypt_str

import os
import shutil

def repo_setup(repo_url, repo_name, version, git_user, git_email, git_pass):
    """
    Clones and tags repository referenced in the POST for /repos
    """
    str = f"{repo_url[:8]}{git_user}:{decrypt_str(git_pass)}@{repo_url[8:len(repo_url)]}"
    repo = Repo.clone_from(str, os.path.join(os.environ.get('GIT_REPOSITORY_PATH'), repo_name))
    repo.config_writer().set_value("user", "name", git_user).release()
    repo.config_writer().set_value("user", "email", git_email).release()
    new_tag = repo.create_tag(version, message='Automatic tag "{0}"'.format(version))
    repo.remotes.origin.push(new_tag)


def repo_delete(repo_name):
    """
    Deletes repository from git repositories path
    """
    shutil.rmtree(os.path.join(os.environ.get('GIT_REPOSITORY_PATH'), repo_name))
