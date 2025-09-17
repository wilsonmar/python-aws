# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is an AWS CDK (Cloud Development Kit) Python project for Infrastructure as Code (IaC) development. The project uses AWS CDK v2 with Python to define and deploy AWS cloud infrastructure.

## Architecture

### Core Components

- **`app.py`**: Entry point that initializes the CDK application and instantiates the main stack
- **`aws_proj/aws_proj_stack.py`**: Main CDK stack class (`AwsProjStack`) where AWS resources are defined
- **`cdk.json`**: CDK configuration file that specifies how to execute the app and includes feature flags
- **`tests/unit/`**: Unit tests for stack validation using CDK assertions

### Project Structure

```
python-aws/
├── app.py                    # CDK app entry point
├── aws_proj/                 # Main CDK stack module
│   ├── __init__.py
│   └── aws_proj_stack.py     # Stack definition
├── tests/unit/               # Unit tests
│   └── test_aws_proj_stack.py
├── requirements.txt          # Production dependencies
├── requirements-dev.txt      # Development dependencies
└── cdk.json                 # CDK configuration
```

The project follows standard AWS CDK patterns with a single stack (`AwsProjStack`) that can be extended to include AWS resources like Lambda functions, S3 buckets, DynamoDB tables, etc.

## Environment Setup

### Python Virtual Environment
```bash
# Create virtual environment
python3 -m venv .venv

# Activate (macOS/Linux)
source .venv/bin/activate

# Activate (Windows) 
source.bat  # or .venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### AWS Configuration
Ensure AWS credentials are configured via:
- AWS CLI: `aws configure`
- Environment variables: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`
- IAM roles (when running on EC2/ECS)

## Common Development Commands

### CDK Operations
```bash
# List all stacks
cdk ls

# Synthesize CloudFormation template
cdk synth

# Deploy stack to AWS
cdk deploy

# Compare deployed stack with current state
cdk diff

# Destroy the stack
cdk destroy

# Bootstrap CDK (first-time setup per account/region)
cdk bootstrap

# Watch mode for continuous synthesis during development
cdk watch
```

### Testing
```bash
# Run unit tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/unit/test_aws_proj_stack.py

# Run tests with verbose output
python -m pytest -v

# Run tests with coverage
python -m pytest --cov=aws_proj tests/
```

### Development Workflow
```bash
# Validate syntax and run tests
python -m pytest tests/

# Synthesize to check for errors
cdk synth

# Compare changes before deployment
cdk diff

# Deploy changes
cdk deploy
```

## CDK Development Patterns

### Adding Resources
- Define AWS resources in `aws_proj/aws_proj_stack.py` using CDK constructs
- Import necessary CDK modules at the top of the file
- Add resources in the `__init__` method of `AwsProjStack`

### Environment Configuration
- Environment-specific deployments can be configured in `app.py`
- Use environment variables or CDK context for configuration
- Feature flags are managed in `cdk.json` context section

### Stack Dependencies
- For multi-stack applications, define stack dependencies in `app.py`
- Use CDK construct sharing patterns for cross-stack references

## Python Version

This project uses Python 3.12 for compatibility with TensorFlow and modern AWS CDK features.