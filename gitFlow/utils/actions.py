from git import Repo, InvalidGitRepositoryError, GitCommandError

from rest_framework import status
from rest_framework.response import Response

from .cryptography import decrypt_str
from gitFlow.models import GitRepos

import os
import shutil

def repo_setup(data):
    """
    Clones and tags repository referenced in the POST for /repos
    """
    git_repository_path = os.path.join(os.environ.get('GIT_REPOSITORY_PATH'), data['name'])
    git_pass = decrypt_str(data['git_pass'])

    if data['secure']:
        str = f"{data['url'][:8]}{data['git_user']}:{git_pass}@{data['url'][8:len(data['url'])]}"
    else:
        str = f"{data['url'][:7]}{data['git_user']}:{git_pass}@{data['url'][7:len(data['url'])]}"

    try:
        repo = Repo.clone_from(str, git_repository_path)
        repo.config_writer().set_value("user", "name", data['git_user']).release()
        repo.config_writer().set_value("user", "email", data['git_email']).release()
        new_tag = repo.create_tag(data['current_version'], message='Automatic tag "{0}"'.format(data['current_version']))
        repo.remotes.origin.push(new_tag)
        repo.remotes.origin.set_url(data['url'])
    except Exception as e:
        shutil.rmtree(git_repository_path)
        raise e


def repo_delete(repo_name):
    """
    Deletes repository from git repositories path
    """
    shutil.rmtree(os.path.join(os.environ.get('GIT_REPOSITORY_PATH'), repo_name))


def repo_update(data, repo_name):
    """
    Updates Repository state dependent upon the data

    name: change the folder name within '${GIT_REPOSITORY_PATH}/repository'
    git_user: update config's user.name
    git_email: update config's user.email
    else: raise ValueError
    """
    repo = Repo(os.path.join(os.environ.get('GIT_REPOSITORY_PATH'), repo_name))
    if 'url' in data or 'secure' in data:
        raise ValueError("URL's, Passwords, and Protocol cannot be updated in this manner")

    if 'name' in data:
        obj = GitRepos.objects.get(name=repo_name)
        src = os.path.join(os.environ.get('GIT_REPOSITORY_PATH'), getattr(obj, 'name'))
        dest = os.path.join(os.environ.get('GIT_REPOSITORY_PATH'), data['name'])
        os.rename(src, dest)
        repo = Repo(dest)

    if 'git_user' in data:
        repo.config_writer().set_value("user", "name", data['git_user']).release()

    if 'git_email' in data:
        repo.config_writer().set_value("user", "email", data['git_email']).release()
