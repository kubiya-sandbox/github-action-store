from pydantic import BaseModel

class CreateIssueParams(BaseModel):
    repo_name: str
    title: str
    body: str

class CreateIssueResponse(BaseModel):
    issue_url: str
    # Other fields from issue.raw_data

class CloseIssueParams(BaseModel):
    repo_name: str
    issue_number: int

class CloseIssueResponse(BaseModel):
    success: bool

class GetIssueParams(BaseModel):
    repo_name: str
    issue_number: int

class GetIssueResponse(BaseModel):
    issue_url: str
    title: str
    body: str
    state: str
