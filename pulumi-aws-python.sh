#!/usr/bin/env bash

# pulumi-aws-python.sh

last_change="25-09-30 v001 new :pulumi-aws-python.sh"

# Like for az = https://www.youtube.com/watch?v=BxMcnBC7xfo = demo
# https://www.pulumi.com/docs/esc/
# Pulumi ESC (Environments, Secrets and Configuration) is a centralized cloud service to
# manage secrets and orchestrate resources in the Pulumi Cloud environments.
# Each environment is a managed collection of static and dynamic settings used to configure 
# any project, stack, application, or service, including
# with short-lived cloud credentials through OpenID Connect.
# https://www.pulumi.com/docs/esc/get-started/

# TODO: Install utilities: XCode Command, Homebrew, Git, etc.

# TODO: Navigate to a folder to receive a new folder.
# TODO: Download this repo to your local macOS laptop:

# TODO: Edit config file to customize variables:
PULUMI_ORG="og2"
PULUMI_PROJ="proj1"
PULUMI_FILEPATH="~/pulumi-$PULUMI_PROJ"
PULUMI_TEMPLATE="aws-python"

# Set default destination org for all stack operations
pulumi org set-default "$PULUMI_ORG"

# TODO: Load config variables into this CLI:
# TODO: Navigate to the PULUMI_FILEPATH folder.
pwd
echo "here to ${PULUMI_FILEPATH}"
cd ~
mkdir -p "${PULUMI_FILEPATH}"
cd "${PULUMI_FILEPATH}"

echo -e "\n\e[4m ls -al at $PWD >>>>\e[0m"
ls -al "${PULUMI_FILEPATH}"

# View backend, current stack, pending operations, and versions:
echo -e "\n\e[4m$pulumi about \e[0m"
pulumi about
exit


# Create a new project from template:
pulumi new "$PULUMI_TEMPLATE" --yes
# Confirm by listing Pulumi Stacks state:
pulumi stack ls -a

pulumi stack select dev

exit


# Login AWS: using AWS credentials (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY).
# TODO: aws login

# If template exists:
pulumi up
# FIXME: diagnostics at https://app.pulumi.com/og2/pulumi-proj1/dev/previews/14824490-ef58-46c1-82df-430d24934f59?explainFailure

# View in Browser (Ctrl+O): https://app.pulumi.com/og2/pulumi-proj1/dev/previews/14824490-ef58-46c1-82df-430d24934f59

exit

