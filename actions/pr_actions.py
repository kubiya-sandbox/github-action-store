from github import GithubException, PullRequest
from ..github_wrapper import get_github_instance, get_entity
from ..models.pull_request import (
    ListOpenPRsParams, ListOpenPRsResponse,
    GetPRDetailsParams, GetPRDetailsResponse, GetRepoPullRequestsParams, GetRepoPullRequestsResponse, PullRequestModel,
    MergePRParams, MergePRResponse
)
from .. import action_store as action_store
import logging

logger = logging.getLogger(__name__)

@action_store.kubiya_action()
def get_pr_details(params: GetPRDetailsParams) -> GetPRDetailsResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)
        pr = repo.get_pull(params.pr_number)
        
        return GetPRDetailsResponse(pr_url=pr.html_url, title=pr.title, body=pr.body or "EMPTY BODY", state=pr.state)
    except GithubException as e:
        logger.error(f"Failed to get pull request details: {e}")
        raise
@action_store.kubiya_action()
def get_repo_pull_requests(params: GetRepoPullRequestsParams) -> GetRepoPullRequestsResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)
        prs = []
        for pr in repo.get_pulls(state=params.state):
            pr_model = PullRequestModel(
                html_url=pr.html_url,
                title=pr.title,
                state=pr.state,
                created_at=str(pr.created_at),
                updated_at=str(pr.updated_at),
                merged=pr.merged,
                merged_at=str(pr.merged_at),
                merge_commit_sha=pr.merge_commit_sha or ""
            )
            prs.append(pr_model)
        return GetRepoPullRequestsResponse(prs=prs)
    except GithubException as e:
        logger.error(f"Failed to get pull requests: {e}")
        raise

@action_store.kubiya_action()
def merge_pr(params: MergePRParams) -> MergePRResponse:
    try:
        github = get_github_instance()
        entity = get_entity(github)
        repo = entity.get_repo(params.repo_name)
        pr = repo.get_pull(params.pr_number)

        # Validate the merge_method
        valid_merge_methods = ["merge", "squash", "rebase"]
        if params.merge_method not in valid_merge_methods:
            raise ValueError(f"Invalid merge method. Allowed methods: {valid_merge_methods}")

        # Merge the pull request with the specified merge method
        merge_commit = pr.merge(commit_message=params.commit_message, merge_method=params.merge_method)

        return MergePRResponse(message=f"Pull request #{params.pr_number} merged successfully. Commit SHA: {merge_commit.sha}")
    except GithubException as e:
        logger.error(f"Failed to merge pull request: {e}")
        raise