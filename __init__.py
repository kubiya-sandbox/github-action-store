from kubiya import ActionStore

action_store = ActionStore("github", "0.1.0")

action_store.uses_secrets(["GITHUB_ORGANIZATION", "GITHUB_TOKEN"])