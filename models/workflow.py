from typing import List
from pydantic import BaseModel, Field


class ListWorkflowRunsParams(BaseModel):
    repo_name: str = Field(..., description="Name of the repository")


class WorkflowRunModel(BaseModel):
    id: str = Field(..., description="ID of the workflow run")
    workflow_name: str = Field(..., description="Name of the workflow")
    created_at: str = Field(..., description="Timestamp when the workflow run was created")
    updated_at: str = Field(..., description="Timestamp when the workflow run was last updated")
    status: str = Field(..., description="Status of the workflow run")
    conclusion: str = Field(..., description="Conclusion of the workflow run")


class ListWorkflowRunsResponse(BaseModel):
    workflow_runs: List[WorkflowRunModel] = Field(..., description="List of workflow runs")


class TriggerWorkflowParams(BaseModel):
    repo_name: str = Field(..., description="Name of the repository")
    workflow_id: str = Field(..., description="ID of the workflow to trigger")
    event_type: str = Field(..., description="Type of the event to trigger the workflow")


class TriggerWorkflowResponse(BaseModel):
    workflow_run_id: str = Field(..., description="ID of the triggered workflow run")
    workflow_run_url: str = Field(..., description="URL of the triggered workflow run")


class GetWorkflowRunParams(BaseModel):
    repo_name: str = Field(..., description="Name of the repository")
    workflow_run_id: str = Field(..., description="ID of the workflow run to retrieve")


class GetWorkflowRunResponse(BaseModel):
    workflow_run_id: str = Field(..., description="ID of the workflow run")
    workflow_run_url: str = Field(..., description="URL of the workflow run")
    status: str = Field(..., description="Status of the workflow run")
    conclusion: str = Field(..., description="Conclusion of the workflow run")


class CancelWorkflowRunParams(BaseModel):
    repo_name: str = Field(..., description="Name of the repository")
    workflow_run_id: str = Field(..., description="ID of the workflow run to cancel")


class CancelWorkflowRunResponse(BaseModel):
    message: str = Field(..., description="Confirmation message after canceling the workflow run")


class TrackWorkflowRunParams(BaseModel):
    repo_name: str = Field(..., description="Name of the repository")
    workflow_run_id: str = Field(..., description="ID of the workflow run to track")
    polling_interval: int = Field(5, description="Interval in seconds to poll the workflow run status")


class TrackWorkflowRunResponse(BaseModel):
    workflow_run_id: str = Field(..., description="ID of the tracked workflow run")
    workflow_run_url: str = Field(..., description="URL of the tracked workflow run")
    status: str = Field(..., description="Status of the tracked workflow run")
    conclusion: str = Field(..., description="Conclusion of the tracked workflow run")
    is_completed: bool = Field(..., description="Flag indicating if the workflow run is completed")


class ListWorkflowFilesParams(BaseModel):
    repo_name: str = Field(..., description="Name of the repository")


class WorkflowFileModel(BaseModel):
    name: str = Field(..., description="The name of the workflow file")
    path: str = Field(..., description="Path of the workflow file")
    size: int = Field(..., description="Size of the workflow file")
    url: str = Field(..., description="URL to access the workflow file")


class ListWorkflowFilesResponse(BaseModel):
    workflow_files: List[WorkflowFileModel] = Field(..., description="List of workflow files")


class GetWorkflowFileParams(BaseModel):
    repo_name: str = Field(..., description="Name of the repository")
    file_path: str = Field(..., description="Path of the workflow file to retrieve")


class GetWorkflowFileResponse(BaseModel):
    path: str = Field(..., description="Path of the retrieved workflow file")
    size: int = Field(..., description="Size of the retrieved workflow file")
    url: str = Field(..., description="URL to access the retrieved workflow file")
    content: str = Field(..., description="Content of the retrieved workflow file")


class ListWorkflowJobRunsParams(BaseModel):
    repo_name: str = Field(..., description="Name of the repository")
    workflow_run_id: str = Field(..., description="ID of the workflow run")


class WorkflowJobRunModel(BaseModel):
    id: str = Field(..., description="ID of the workflow job run")
    name: str = Field(..., description="Name of the workflow job")
    status: str = Field(..., description="Status of the workflow job run")
    conclusion: str = Field(..., description="Conclusion of the workflow job run")


class ListWorkflowJobRunsResponse(BaseModel):
    job_runs: List[WorkflowJobRunModel] = Field(..., description="List of workflow job runs")


class GetWorkflowJobRunParams(BaseModel):
    repo_name: str = Field(..., description="Name of the repository")
    workflow_run_id: str = Field(..., description="ID of the workflow run")
    job_id: str = Field(..., description="ID of the job run to retrieve")


class GetWorkflowJobRunResponse(BaseModel):
    job_run_id: str = Field(..., description="ID of the job run")
    job_name: str = Field(..., description="Name of the job")
    status: str = Field(..., description="Status of the job run")
    conclusion: str = Field(..., description="Conclusion of the job run")


class DownloadWorkflowArtifactParams(BaseModel):
    repo_name: str = Field(..., description="Name of the repository")
    workflow_run_id: str = Field(..., description="ID of the workflow run")
    artifact_name: str = Field(..., description="Name of the artifact to download")


class DownloadWorkflowArtifactResponse(BaseModel):
    download_url: str = Field(..., description="URL to download the workflow artifact")


class ListWorkflowPullRequestsParams(BaseModel):
    repo_name: str = Field(..., description="Name of the repository")
    workflow_run_id: str = Field(..., description="ID of the workflow run")


class WorkflowPullRequestModel(BaseModel):
    number: int = Field(..., description="Number of the pull request")
    title: str = Field(..., description="Title of the pull request")
    url: str = Field(..., description="URL of the pull request")
    state: str = Field(..., description="State of the pull request")
    head_branch: str = Field(..., description="Branch name from which the pull request originates")
    base_branch: str = Field(..., description="Target branch of the pull request")


class ListWorkflowPullRequestsResponse(BaseModel):
    pull_requests: List[WorkflowPullRequestModel] = Field(..., description="List of pull requests associated with the workflow run")

class WorkflowFileModel(BaseModel):
    name: str = Field(..., description="Name of the workflow file")
    path: str = Field(..., description="Path of the workflow file")
    size: int = Field(..., description="Size of the workflow file")
    url: str = Field(..., description="URL to access the workflow file")


class GetWorkflowFileContentParams(BaseModel):
    repo_name: str = Field(..., description="Name of the repository")
    file_path: str = Field(..., description="Path of the workflow file to retrieve content")


class GetWorkflowFileContentResponse(BaseModel):
    content: str = Field(..., description="Content of the retrieved workflow file")


class GetWorkflowFileContentRawParams(BaseModel):
    repo_name: str = Field(..., description="Name of the repository")
    file_path: str = Field(..., description="Path of the workflow file to retrieve raw content")


class GetWorkflowFileContentRawResponse(BaseModel):
    content: bytes = Field(..., description="Raw content of the retrieved workflow file")


class GetWorkflowFileContentRawParams(BaseModel):
    repo_name: str = Field(..., description="Name of the repository")
    file_path: str = Field(..., description="Path of the workflow file to retrieve raw content")


class GetWorkflowFileContentRawResponse(BaseModel):
    content: bytes = Field(..., description="Raw content of the retrieved workflow file")

class ListWorkflowJobRunsParams(BaseModel):
    repo_name: str = Field(..., description="Name of the repository")
    workflow_run_id: str = Field(..., description="ID of the workflow run")


class GetWorkflowJobRunResponse(BaseModel):
    job_run_id: str = Field(..., description="ID of the job run")
    job_name: str = Field(..., description="Name of the job")
    status: str = Field(..., description="Status of the job run")
    conclusion: str = Field(..., description="Conclusion of the job run")

class GetWorkflowJobRunResponse(BaseModel):
    job_run_id: str = Field(..., description="ID of the job run")
    job_name: str = Field(..., description="Name of the job")
    status: str = Field(..., description="Status of the job run")
    conclusion: str = Field(..., description="Conclusion of the job run")

class GetWorkflowJobRunResponse(BaseModel):
    job_run_id: str = Field(..., description="ID of the job run")
    job_name: str = Field(..., description="Name of the job")
    status: str = Field(..., description="Status of the job run")
    conclusion: str = Field(..., description="Conclusion of the job run")

class DownloadWorkflowArtifactResponse(BaseModel):
    download_url: str = Field(..., description="URL to download the workflow artifact")

class ListWorkflowPullRequestsParams(BaseModel):
    repo_name: str = Field(..., description="Name of the repository")
    workflow_run_id: str = Field(..., description="ID of the workflow run")

class DownloadWorkflowArtifactParams(BaseModel):
    repo_name: str = Field(..., description="Name of the repository")
    workflow_run_id: str = Field(..., description="ID of the workflow run")
    artifact_name: str = Field(..., description="Name of the artifact to download")
