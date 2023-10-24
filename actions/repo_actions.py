from github import GithubException, UnknownObjectException, ContentFile
import logging

from ..models.branch import CreateBranchParams, CreateBranchResponse
from ..github_wrapper import get_github_instance, get_entity
from ..models.repository import (
    FindRepositoriesParams, FindRepositoriesResponse,
    GetRepoBranchesParams, GetRepoBranchesResponse,
    CreateRepoParams, CreateRepoResponse,
    DeleteRepoParams, DeleteRepoResponse,
    GetRepoFilesParams, GetRepoFilesResponse,
    CreatePullRequestParams, CreatePullRequestResponse
)
from ..models.repository import (
    ListRepositoriesParams, ListRepositoriesResponse
)
from .. import action_store as action_store

logger = logging.getLogger(__name__)

@action_store.kubiya_action()
def create_repo(params: CreateRepoParams) -> CreateRepoResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.create_repo(params.repo_name)
        return CreateRepoResponse(repo_url=repo.html_url, **repo.raw_data)
    except GithubException as e:
        logger.error(f"Failed to create repository: {e}")
        raise

@action_store.kubiya_action()
def delete_repo(params: DeleteRepoParams) -> DeleteRepoResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)
        repo.delete()
        return DeleteRepoResponse(success=True)
    except GithubException as e:
        logger.error(f"Failed to delete repository: {e}")
        raise

@action_store.kubiya_action()
def get_repo_files(params: GetRepoFilesParams) -> GetRepoFilesResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)
        contents = repo.get_contents("")
        files = [content.path for content in contents if isinstance(content, ContentFile.ContentFile)]
        return GetRepoFilesResponse(files=files)
    except GithubException as e:
        logger.error(f"Failed to get repository files: {e}")
        raise

@action_store.kubiya_action()
def create_pull_request(params: CreatePullRequestParams) -> CreatePullRequestResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)
        pull_request = repo.create_pull(
            title=params.title,
            body=params.body,
            head=params.branch_name,
            base='master'
        )
        return CreatePullRequestResponse(pull_request_url=pull_request.html_url, **pull_request.raw_data)
    except GithubException as e:
        logger.error(f"Failed to create pull request: {e}")
        raise

@action_store.kubiya_action()
def get_repo_branches(params: GetRepoBranchesParams) -> GetRepoBranchesResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)
        branches = [branch.name for branch in repo.get_branches()]
        return GetRepoBranchesResponse(branches=branches)
    except GithubException as e:
        logger.error(f"Failed to get repository branches: {e}")
        raise

@action_store.kubiya_action()
def list_repos(params: ListRepositoriesParams) -> ListRepositoriesResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repos = [repo.name for repo in entity.get_repos()]
        return ListRepositoriesResponse(repos=repos)
    except GithubException as e:
        logger.error(f"Failed to list repositories: {e}")
        raise

@action_store.kubiya_action()
def list_repos(params: ListRepositoriesParams) -> ListRepositoriesResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repos = [repo.name for repo in entity.get_repos()]
        return ListRepositoriesResponse(repos=repos)
    except GithubException as e:
        logger.error(f"Failed to list repositories: {e}")
        raise

@action_store.kubiya_action()
def find_repos(params: FindRepositoriesParams) -> FindRepositoriesResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repos = [repo.name for repo in entity.get_repos() if params.pattern in repo.name]
        return FindRepositoriesResponse(repos=repos)
    except GithubException as e:
        logger.error(f"Failed to find repositories: {e}")
        raise

@action_store.kubiya_action()
def create_branch(params: CreateBranchParams) -> CreateBranchResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)
        base_sha = repo.get_branch(params.base_branch).commit.sha
        repo.create_git_ref(ref='refs/heads/' + params.branch_name, sha=base_sha)
        return CreateBranchResponse(message=f'Branch {params.branch_name} created successfully in {params.repo_name} repo')
    except GithubException as e:
        print(f"Failed to create branch: {e}")
        return CreateBranchResponse(message=f'Error: {str(e)}')