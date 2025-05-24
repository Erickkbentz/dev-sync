## Command List

### `dev-sync init`
Initialize a new `devsync_config.yaml` based on your current machine’s environment and settings.


### `dev-sync add-secret`
Add a new secret to AWS Secrets Manager and update the config file.


### `dev-sync add-private-file`
Upload a private file to S3 and update the config file.


### `dev-sync commit`
Commit the current `devsync_config.yaml` (and related metadata) to your Git repository.


### `dev-sync pull`
Pull the latest config from your Git repository.

### `dev-sync sync`
Sync your machine to match the `devsync_config.yaml`
