from pydantic import BaseModel
from typing import List

class ListRepositoriesParams(BaseModel):
    pass

class ListRepositoriesResponse(BaseModel):
    repos: List[str]


class CreateRepoParams(BaseModel):
    repo_name: str

class CreateRepoResponse(BaseModel):
    repo_url: str
    # Other fields from repo.raw_data

class DeleteRepoParams(BaseModel):
    repo_name: str

class DeleteRepoResponse(BaseModel):
    success: bool

class GetRepoFilesParams(BaseModel):
    repo_name: str

class GetRepoFilesResponse(BaseModel):
    files: list

class CreatePullRequestParams(BaseModel):
    repo_name: str
    title: str
    body: str
    src_branch: str
    dest_branch: str

class CreatePullRequestResponse(BaseModel):
    pull_request_url: str


class ListRepositoriesParams(BaseModel):
    pass

class ListRepositoriesResponse(BaseModel):
    repos: List[str]

class FindRepositoriesParams(BaseModel):
    pattern: str

class FindRepositoriesResponse(BaseModel):
    repos: List[str]

class GetRepoBranchesParams(BaseModel):
    repo_name: str

class GetRepoBranchesResponse(BaseModel):
    branches: List[str]