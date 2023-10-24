from pydantic import BaseModel

class CreateBranchParams(BaseModel):
    repo_name: str
    branch_name: str
    base_branch: str

class CreateBranchResponse(BaseModel):
    message: str