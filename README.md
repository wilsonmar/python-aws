---
layout: post
lastchange: "25-09-18 v024 + aws cli :README.md"
url: "https://github.com/wilsonmar/python-aws/blob/main/README.md"
---

This repo guides Python developers to use AWS cloud resources securely and efficiently
by leveraging the <a href="#AWS_CLI">AWS CLI</a>, <a href="#AWS_CDK">AWS CDK</a>, and the <a href="#Boto3">AWS Boto3</a> (among other <a href="#Libraries">Python libraries</a>).

This README adapts instructions from AWS with use of uv instead of pip.
https://realpython.com/videos/run-project-with-uv/

## Program run parameters

For quick reference here, after successful <a href="#installation"> and <a href="#configuration">configuration</a> described below:

The programs can be run using a choice of several ways:

| command | Note |
| -------------------------- | ---- |
| <tt>./app.py</tt> | References the first line of the file to specify the Python interpreter. |
| <tt>python run app.py</tt> | Invokes the Python interpreter and ignore that first interpreter line. |
| <tt>uv run app.py</tt> | Invokes the uv package manager utility to automatically resolve package dependencies. |

The last option above is our recommended approach. 

The default standard output from the program is to show what is commonly known as 
<strong>INFO</strong> level information that satisfies the objective of the program.
For example, <a target="_blank" href="https://github.com/aws-samples/aws-cdk-examples/tree/main/python/url-shortener">sample code from AWS</a> creates shortened URLs by building a Lambda function, as <a target="_blank" href="https://www.youtube.com/watch?v=ZWCvNFUN-sU" title="from 2020">described by its creators</a>.

The most run common commands and parameters during development is:
```
uv run app.py -v -vv -s
```
Parameters to control programs:
| abbr. | Parm | Explanation |
| ------- | ---- | --------- |
| <tt>-s</tt> | <tt>\-\-summary</tt> | Show summary statistics at the beginning and end of the run. |
| <tt>-q</tt> | <tt>\-\-quiet</tt> | Withhold INFO, ERROR, FATAL, summary messages. |
| <tt>-v</tt> | <tt>\-\-verbose</tt> | Show messages about internal calculations for debugging, such as the path of input and output files. |
| <tt>-vv</tt> | <tt>\-\-debug</tt> | Show details for debugging. |
| <tt>-L</tt> | <tt>\-\-log</tt> | Log events to a telemetry system (used during productive runs). |
| <tt>-a</tt> | <tt>\-\-alert</tt> | Send alerts (used during productive runs). |
| <tt>-e</tt> | <tt>\-\-env</tt> <em>filepath</em> | Override the path to default <tt>.env</tt> file  containing configuration settings and secrets (API keys). |
| <tt>-D</tt> | <tt>\-\-destroy</tt> | Destroy resources after processing. |

Sample results returned:
```
app.py started: 2025-09-16 19:06:18.153274Z
DEBUG: psutil.Process(pid=13849, name='Python', status='running', started='19:06:15')
DEBUG: pgm_memory used()=414.84375 MiB being used.
DEBUG: pgm_diskspace_free()=368.20 GB
0.046875 MB memory consumed during run in psutil.Process(pid=13849, name='Python', status='running', started='19:06:15').
0.000042 GB disk space consumed during run.
SUMMARY: Ended while attempting loop 0 in 0:00:00.092067 seconds.
```
<tt>Z</tt> in dates signify that the date is set to UTC/GMT time zone so that all servers would issue  timestamps that would not have potential errors from going back and forth Daylight Savings Summertime.

<hr />

<a name="installation"></a>

## Install utilities:

This program was tested to be installed and run on macOS, Raspian Linux, and Windows 10 & 11.

1. Install package manager: On macOS, it's Homebrew:
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   on Windows, it's Chocolatey:
   ```
   ???
   ```
   on Raspian:
   ```
   # Update package index and install pip if needed (Debian/Ubuntu example)
   sudo apt update
   sudo apt install -y python3-pip
   ```
   on RedHat:
   ```
   sudo su -
   yum install gcc openssl-devel bzip2-devel libffi-devel
   ```
1. Install GitHub utilities:
   ```
   brew install git
   brew install gh
   ```
1. Setup SSH in GitHub. ???

1. Setup SSH for GitHub signing of verified commits.

1. Install NodeJs which comes with npm (Node Package Manager) used by <a href="#AWS_CDK">AWS CDK (Cloud Development Kit)</a>:
   On macOS:
   ```
   brew info node
   brew install node    # from https://nodejs.org/
   ```
   On Linux:
   ```
   sudo apt install -y nodejs npm
   ```
1. Install AWS-CDK using NPM, on all platforms:
   ```
   npm install -g aws-cdk
   ```
1. Verify CDK:   
   ```
   cdk --version
   2.1029.1 (build b45b1ab)
   ```
1. Confirm Python
   ```
   python --version
   ```
   Python 3.13.6

   NOTE: The preferred version is defined in the <tt>pyproject.toml</tt> file.


<a name="AWS_CDK"></a>

## What is the AWS CDK?

<a target="_blank" href="https://res.cloudinary.com/dcajqrroq/image/upload/v1758103412/aws-cdk-1920x500_y4gmau.png"><img alt="aws-cdk-1920x500.png" src="https://res.cloudinary.com/dcajqrroq/image/upload/v1758103412/aws-cdk-1920x500_y4gmau.png" /></a>

<a target="_blank" href="https://res.cloudinary.com/dcajqrroq/image/upload/v1758094660/aws-cdk-AppStacks-774x576_jsdljc.png"><img alt="aws-cdk-AppStacks-774x576.png" src="https://res.cloudinary.com/dcajqrroq/image/upload/v1758094660/aws-cdk-AppStacks-774x576_jsdljc.png" /></a>

<a target="_blank" href="https://www.youtube.com/watch?v=D4Asp5g4fp8" title="from 2024">VIDEO</a>: "AWS CDK Crash Course for Beginners" (using TypeScript), followup to <a target="_blank" href="https://www.youtube.com/watch?v=I2cXlYYoQqQ">this from 2021</a>. <a target="_blank" href="https://www.youtube.com/watch?v=AYYTrDaEwLs&pp=0gcJCcoJAYcqIYzv">CTO Werner Vogels explains</a>.

Amazon created their <a target="_blank" href="https://docs.aws.amazon.com/cdk/v2/guide/home.html"><strong>proprietary</strong></a> platform illustrated above</a> to enable access into the vast variety of AWS cloud resources using several application programming languages: TypeScript, JavaScript, Java, C# (.NET), Go, as well as Python, as described in the <a target="_blank" href="https://docs.aws.amazon.com/cdk/v2/guide/work-with.html">AWS CDK Developer Guide</a> and <a target="_blank" href="https://docs.aws.amazon.com/cdk/v2/guide/how-tos.html">How-To</a>.

App code define, for a <strong>user accounts</strong> within designated <strong>regions</strong>, one or more <strong>Constructs</strong> defined to manage AWS cloud resources such as S3 buckets, SQS, Lambda, DynamoDB databases, etc. Details about the full range of each resource managed by CDK is in its <a target="_blank" href="https://docs.aws.amazon.com/cdk/api/v2/python/">API Reference</a>.

Each of one or more <strong>Stacks</strong> group constructs, such as "Storage", "Dashboard", etc.

<a name="Synthesize"></a>

Stacks and Construct definitions are "synthesized" to AWS proprietary CloudFormation template files which AWS excutes to create and manage actual resources in the AWS Cloud.

<a target="_blank" href="https://res.cloudinary.com/dcajqrroq/image/upload/v1758097353/aws-diagram-767x525_wrcd0s.png"><img alt="aws-diagram-767x525" src="https://res.cloudinary.com/dcajqrroq/image/upload/v1758097353/aws-diagram-767x525_wrcd0s.png" /></a>

Due to its complexity, among <a target="_blank" href="https://github.com/aws-samples/aws-cdk-examples/tree/main/python">Sample CDK Python programs</a> is <a target="_blank" href="https://github.com/aws-samples/aws-cdk-examples/tree/main/python/cdk-validator-cfnguard">How to enable</a> the (still "experimental") <a target="_blank" href="https://github.com/cdklabs/cdk-validator-cfnguard">CDK Validator for CFNGuard</a> of <a target="_blank" href="https://docs.aws.amazon.com/controltower/latest/controlreference/proactive-controls.html">Proactive Controls</a> enforced by the <a target="_blank" href="https://docs.aws.amazon.com/controltower/latest/userguide/proactive-controls.html">AWS Control Tower</a>, which can stop the deployment of non-compliant resources deployed via CloudFormation.

AWS CDK reduces the complexity by code such as this:<br />
<a target="_blank" href="https://res.cloudinary.com/dcajqrroq/image/upload/v1758097350/aws-cdk-cmds-1082x614_kuogee.png"><img alt="" src="https://res.cloudinary.com/dcajqrroq/image/upload/v1758097350/aws-cdk-cmds-1082x614_kuogee.png" /></a> 

Constructs can be defined at three levels of specificity (detail level).
* Level 1 (L1) is low-level where everything can be specified. Most don't go here.
* Level 2 (L2) is the "curated" level of "sensible" defaults, Security Best Practices, and helper methods which can be overrrided. Most commonly work at this level.
* Level 3 (L3) are called "Patterns" that define a whole pre-made architecture.
<br /><br />

PROTIP: Alternatives to AWS CDK is <a target="_blank" href="https://wilsonmar.github.io/terraform/Terraform">Terraform</a>, which are <strong>declarative</strong> statements of static cloud resources, so utilities can check for security issues even before the resources are provisioned.

HashiCorp also developed the dynamic code "CDK for Terraform" to compete with <a target="_blank" href="https://wilsonmar.github.io/Pulumi">Pulumi</a>. Each of those platforms support other cloud and SaaS providers using <a target="_blank" href="https://www.pulumi.com/docs/iac/concepts/vs/cloud-template-transpilers/aws-cdk/">similar techniques</a>. <a target="_blank" href="https://www.site24x7.com/learn/aws/aws-cdk-pulumi-comparison.html">This detailed comparison</a>.

The Construct Hub website at <a target="_blank" href="https://constructs.dev/">https://constructs.dev/</a> has crowd-sourced example code for several platforms in one place.

QUESTION: Vide coding and MCP agents?



<hr />

<a name="DownloadRepo"></a>

## Download python-aws repo

1. Open a Terminal to create a project folder to hold this project:
   ```
   cd "$HOME"
   cd wilsonmar        # folder holding all repos within my github account.
   ```
1. Clone
   ```
   git clone https://github.com/wilsonmar/python-aws
   cd python-aws
   ```
   The repo contains files created based on following 
   https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html
   AWS Cloud Development Kit in the section below.

   <a name="FilesFolders"></a>

1. Notice the files and folders:

   <tt>README.md</tt> (this file describing the repo).
   
   <tt>CONTRIBUTING.md</tt> defines policies and procedures for making git commits and Push Requests to this repo.

   <tt>.editorconfig</tt> (no file extension) defines coding styles and text editor configurations in order to maintain consistentcy for multiple developers working on the same project across various editors and IDEs. It's described at <a target="_blank" href="https://EditorConfig.org">EditorConfig.org</a>.

   <tt>WARP.md</tt> file was created by the Warp CLI utility for its AI assist capabilities.

   <tt>LICENSE</tt> (no file extension) defines the Apache Version 2.0 license governing use of this intellectual property, copied from a template.

1. Click <a href="#configuration">configuration here</a> to skip past the <a href="#BlankCDK">Create Blank CDK project</a> below which describes how the repo was created initially.

<hr />

<a href="#BlankCDK"></a>

## Create Blank CDK project

1. Initialize a blank Python project and initialize AWS CDK project:
   ```
   MY_PROJ_FOLDER="python-aws"   # folder holding the repo for this project.
   mkdir "$MY_PROJ_FOLDER"
   cd "$MY_PROJ_FOLDER"
   pwd               # confirm that you're at like "/Users/johndoe/wilsonmar/python-aws"
   cdk init app --language python
   ls -al
   ```
   Contents of the created folder:
   ```
   .git          # folder to retain history and contains hook scripts
   .gitignore    # 
   .venv         # folder
   <a href="#app.py">app.py</a>       # starter Python program 
   cdk.context.json      # ?
   cdk.json      # tells the CDK Toolkit how to execute your app.
   requirements-dev.txt
   requirements.txt
   source.bat    # for Windows to run.
   python_aws    # folder contains __init.py and python_aws_stock.py
   tests         # folder 
   ```

   Additionally, these are created by uv and pip:
   ```
   .cdk.staging        # CDK asset staging directory
   *.swp
   package-lock.json
   __pycache__
   .pytest_cache
   *.egg-info
    ```
1. Acknowledge:
   ```
   cdk acknowledge 34892
   ```
1. PROTIP: Rename the "master" branch to "main" (to be politically correct).
   ```
   git branch
   git branch -m main
   ```

<a name="ConvertToUV"></a>

## Convert from pip to uv

See <a target="_blank" href="https://www.youtube.com/watch?v=AMdG7IjgSPM">this video</a>
for an explanation of why and how to use uv.

1. PROTIP: To better manage modules, we use the more modern uv utility, which needs to be initialized by this:
   ```
   uv init --no-readme
   ```
   That's instead of <tt>requirements.txt</tt> created and referenced by <tt>pip</tt>.

   <tt>uv init</tt> creates these starter files:
   ```
   .gitignore          # see its contents below.
   .python-version
   main.py             # A "hello world"
   pyproject.toml      # configuration
   README.md           # empty (if created)
   ```
1. Copy the .python-version, main.py, pyproject.toml files to the folder created by aws cdk.

1. Contents of the .gitignore file generated by uv should be combined with the contents of .gitignore generated by aws cdk:
   ```
   # Python-generated files
   __pycache__/
   *.py[oc]
   build/
   dist/
   wheels/
   *.egg-info

   # Virtual environments
   .venv
   ```
1. Files <tt>requirements.txt</tt> and <tt>requirements-dev.txt</tt> can be deleted because we prefer to generate files at the beginning of each work session so that we get the very latest versions of all modules and thus detect integration issues as soon as possible.

<hr />

<a name="configuration"></a>

## Configuration:

<a name="app.py"></a>

## Edit app.py

1. See https://docs.aws.amazon.com/cdk/latest/guide/environments.html

1. Edit file <tt>app.py</tt> to "specialize" the current "stack" consisting of the AWS Account and Region you want to use. But instead of un-commenting the line specifying CDK_DEFAULT_ACCOUNT (such as 123456789012) and CDK_DEFAULT_REGION (such as 'us-east-1').
   ```
   env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
   ```
   <a href="#Libraries"></a>

   ### Python Libraries used

1. We've edited file <tt>app.py</tt> to use a try/exception coding convention to send out a console message when external dependencies have not been imported properly.
   ```
   uv add aws-cdk-lib constructs boto3 putils
   ```

   Technical notes:
   ```
   # This uv dependency metadata for your import of PythonAwsStack, use an inline script header at the top of your Python file. This lets uv automatically manage and install the package needed for the import when you run the script.
   # /// script
   # dependencies = ["python_aws"]
   # ///
   ```

<a name="Pytest"></a>

## Pytest for development

1. For testing: PROTIP: There is some conflict using <tt>aws-cdk-assertions</tt>, so:
   ```
   uv add --dev pytest 
   ```
1. REMEMBER: Pytest looks for and automatically runs function names starting with "test_...".

1. TODO: GenAI that creates test functions.

<hr />

<a name="UseRepo"></a>

##  Use the repository

### Source activate

1. Every time you prepare to run the program, define a virtual environment the new uv way:
   ```
   uv venv .venv
   source .venv/bin/activate
   ```
   That's instead of what AWS recommends in their (outdated) docs:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   On Windows:
   ```
   .venv\Scripts\activate.bat
   ```
1. To download imports specified within the program:
   ```
   uv add aws_cdk
   uv venv .venv
   source .venv/bin/activate
   ```
   Instead of:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   On Windows:
   ```
   .venv\Scripts\activate.bat
   ```

<hr />

<a name="#Diving"></a>

## Diving into AWS

1. <a href="#GUI">AWS URLs and GUI</a> on an internet browser.
1. <a href="#Feduciary">Feduciary responsbilities</a> for email, credit card, and other private info.
1. <a href="#IaC">Infrastructure as Code (IaC)</a> options.

1. <a href="#Roles">Strategies and policies</a> in assiging permissions to working Users and Roles.

   <a target="_blank" href="https://res.cloudinary.com/dcajqrroq/image/upload/v1758097353/aws-diagram-767x525_wrcd0s.png"><img alt="aws-diagram-767x525" src="https://res.cloudinary.com/dcajqrroq/image/upload/v1758097353/aws-diagram-767x525_wrcd0s.png" /></a> 

1. <a href="#LockDownAdmin">Locking down Global Administrator user account</a>.

   PROTIP: Configure a different profile for each point in the system lifecycle.

1. <a href="#Workflows">Workflows for what each user type does</a>.
1. <a href="#AWS_CLI">Install AWS CLI</a> for the IAM Console.

1. <a href="#Secrets">Secrets Manager</a> usage.
1. <a href="#S3">Managing S3 buckets and files</a>.
1. <a href="#Compute">Managing compute environments</a> (EC2 & Fargate).
1. <a href="#RDS">Managing Relational SQL databases</a> (RDS, etc.).

<em>(sections removed for editing)</em>

<hr />


### serverless-admin user


<a name="AWS_Account"></a>

## AWS Account with Limited permissions

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

<a name="Install_AWS_CLI"></a>

1. on macOS, at any folder, install the AWSCLIV2.pkg :
   ```
   brew install awscli
   ```
   on Linux: 
   ```
   curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
   sudo installer -pkg AWSCLIV2.pkg -target /
   ```
   Response:
   ```
   installer: Package name is AWS Command Line Interface
   installer: Installing at base path /
   installer: The install was successful.
   ```
1. Confirm:
   ```
   aws --version
   ```
   At time of writing:
   ```
   aws-cli/2.28.10 Python/3.13.6 Darwin/24.6.0 source/arm64
   ```
1. Verify: on macOS or Linux:
   ```
   which aws
   ```
   /usr/local/bin/aws
   ```
1. PROTIP: Configure a different profile for each point in the system lifecycle.

   This prompts for AWS Access Key ID, Secret Access Key, default region, and output format:
   ```
   aws configure --profile dev
   aws configure --profile qa
   aws configure --profile prod
   ```

1. Interactively configure through the IAM Identity Center: 
   see https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html
   ```
   aws configure sso

   SSO session name (Recommended): my-sso
   SSO start URL [None]: https://my-sso-portal.awsapps.com/start
   SSO region [None]:us-east-1

   Attempting to automatically open the SSO authorization page in your default browser.

   There are 2 AWS accounts available to you.
   > DeveloperAccount, developer-account-admin@example.com (111122223333) 
   ProductionAccount, production-account-admin@example.com (444455556666)

   Using the account ID 111122223333

   There are 2 roles available to you.
   > ReadOnly
   FullAccess

   Using the role name "ReadOnly"

   CLI default client Region [None]: us-west-2
   CLI default output format [None]: json
   CLI profile name [123456789011_ReadOnly]: user1
   ```

<a name="Account"></a>

### AWS Account

1. Confirm:
   ```
   aws sts get-caller-identity
   ```
   The expected response is like:
   ```
   {
       "UserId": "DSDFIVEEIJVKWEWV82",
       "Account": "123456789012",
       "Arn": "arn:aws:iam::448292842/CICDUser"
   }
   ```
1. Bootstrap:
   ```
   cdk bootstrap aws://123456789012/us-west-2
   ```
   The expected response is like:
   ```
   Trusted accounts for deployment: (none)
   Trusted accounts for lookup: (none)
   Using default execution policy of 'arn:aws:iam::aws:policy/AdministratorAccess'. Pass '--cloudformation-execution-policies' to customize.
   ```


<hr />

<a name="Boto3"></a>

## Boto3

https://github.com/aws-samples/aws-cdk-examples/tree/main/python

session, resource,client,collections,waiters and paginators

<hr />


<a name="MyApps"></a>

## apps folder

Within the repo's apps folder: 


1. Use ChatGPT to create <a target="_blank" href="https://www.youtube.com/watch?v=Ps4CmSzRSSs&list=PLqdbsgoG9hwWYlNvMJmt6rLQXaM6MoEAh&index=4">VIDEO</a>
   ```
   You are 
   ```

### url-shortener.py

Based on AWS-samples repo <a target="_blank" href="https://github.com/aws-samples/aws-cdk-examples/tree/main/python/url-shortener">URL Shortener</a>.



### hello-lambda.py




### 01-webotron

Webotron is a script that syncs a local directory to an s3 bucket, and optionally configure Route 53 and cloudfront as well. It has these features:

- List bucket
- List contents of a bucket
- Create and set up bucket
- Sync directory tree to bucket
- Set AWS profile with --profile=<profileName>
- Configure route 53 domain

### 02-notifon

Notify Slack users of changes to your AWS account based on CloudWatch Event triggers.

### 03-videolyzer



### 04-aiops

This folder houses assets from the hands-on tutorial from Courseara 
course: "DevOps and AI on AWS: AIOps" at:
https://www.coursera.org/learn/aiops-aws/
which has these hands-on Tasks using AWS Training instances:

   1. Install and start the ADOT collector (adot1.sh)
   2. Instrument the application with Python OpenTelemetry Auto-instrumentation
   3. Observe X-Ray traces and trace map
   4. Manually setting trace attributes

<hr />



<a name="AWS_CDK_CLI"></a>

### AWS CDK CLI commands

* `cdk help`        list all commands for cdk CLI program
* `cdk docs`        open CDK documentation

* `cdk ls`          list all stacks in the app
* `cdk synth`       emits the synthesized CloudFormation template
* `cdk diff`        compare deployed stack with current state
* `cdk deploy`      <a href="#cdk_deploy">deploy the stack</a> to your default AWS account/region
* `cdk destroy`     <a href="#cdk_destroy">destroy (remove) resources</a>


contains <tt>import aws_cdk as cdk</tt> for <tt>synth</tt> command.
from python_aws.python_aws_stack import PythonAwsStack

<a name="cdksynth"></a>

### CDK app.synth()

What does <tt>app.synth()</tt> do?

1. <a href="#Synthesize">Synthesize</a> the CloudFormation template for the code:
   ```
   cdk synth
   ```
   
   <a name="cdk_deploy"></a>

1. On CLI Terminal: Execute CDK to create resources:
   ```
   cdk deploy
   ```
1. On AWS Console GUI: view resources created

   <a name="ListResources"></a>

1. List resources! From GUI:

   Using Python Boto3 code ???


   <a name="cdk_destroy"></a>

1. Specify a parmeter when executing app.py, such as 

   <tt>-D</tt>

1. On CLI Terminal: Execute CDK to create resources:
   ```
   cdk destroy
   ```
1. On AWS Console GUI: view resources removed.


* `cdk destroy`     <a href="#cdk_destroy">destroy (remove) resources</a>



## Video courses

By DevOps With Namdev on YouTube:
   * <a target="_blank" href="https://www.youtube.com/watch?v=q8kmQndrZJY&list=PLqdbsgoG9hwWYlNvMJmt6rLQXaM6MoEAh">10 VIDEO playlist 2024</a>
   * https://github.com/namdev-rathod/AWS-CDK

By Cloud Quick Labs on YouTube:
   * <a target="_blank" href="https://www.youtube.com/watch?v=yUGNPTGIW1U">VIDEO</a>: AWS CDK in Python | How To Use AWS CDK in Python to Provision AWS Cloud Infrastructure Resource (on Windows)

By Alfredo Deza and Noah Gift from <a target="_blank" href="https://learning.oreilly.com/publisher/003a971a-64f0-4a9e-b7fa-8000623a3e21">Pragmatic AI Labs</a>
   * <a target="_blank" href="https://learning.oreilly.com/videos/-/01242022VIDEOPAIML/">7m AWS CDK 2.8 with Python Deploy Hello World Lambda</a> 2022 (using AWS Cloud9 editor runnig cdk-workshop)
   * <a target="_blank" href="https://learning.oreilly.com/videos/-/10262021VIDEOPAIML/">1hr Hello World IAC with AWS CDK</a> (using TypeScript on AWS Cloud9 editor) 
   * <a target="_blank" href="https://learning.oreilly.com/videos/-/11232022VIDEOPAIML/">Assimilate AWS Cloud Development Kit (CDK)</a> Dec 2022
   <br /><br />

By <a target="_blank" href="https://www.linkedin.com/in/paulo-dichone/">Paulo Dichone</a>
   * <a target="_blank" href="https://learning.oreilly.com/videos/-/9781836646211/">5hr Mastering AWS CDK - Coding Cloud Architectures Sep 20224</a> 

Be A Better Dev:
   * <a target="_blank" href="https://www.youtube.com/watch?v=rKQ68FxY53c">AWS Just Changed Everything: Meet AWS MCP</a> 2026
   * https://youtu.be/D4Asp5g4fp8
   * https://courses.beabetterdev.com/courses/web-scraping-bot
   * <a target="_blank" href="https://www.youtube.com/watch?v=eLIMB0O2LhY">VIDEO: Should you start using AWS CDK?</a>
   * <a target="_blank" href="https://www.youtube.com/watch?v=I2cXlYYoQqQ&pp=ygUHYXdzIGNkaw%3D%3D">Playlist "Getting Started with AWS CDK and Python | Step by Step Tutorial" 2022</a>

Program with Akshay on YouTube:
   * <a target="_blank" href="https://www.youtube.com/watch?v=k5JQAIgDuu0&list=PLaze7fvkDZmiERcSA6bMJpAWoOcQdnl7WP">"AWS CDK MasterClass" Playlist 2024</a> using NodeJs.

Train to Code:
   * <a target="_blank" href="https://www.youtube.com/watch?v=a5_-NwObcgM">"Why Developers Are Switching to AWS CDK"</a>

by Tech With <a target="_blank" href="https://www.linkedin.com/in/yeshwanth-l-m-5b8b9215b/">Yeshwanth</a>
<a target="_blank" href="https://www.youtube.com/playlist?list=PLjl2dJMjkDjlcI3SQErSq4UMX3okzafvO">
AWS Automation with Python Boto3 - 8 video playlist</a>:
   * https://github.com/yeshwanthlm/Boto3-Course-YouTube/tree/main/Project-1
   * https://docs.google.com/document/d/1-34IR_hz1ngwLWET9t5XSwOWEPULcDByQTp0buqJvqk/edit?usp=sharing Notes/Documentation can be found here: 
   * AWS Playlist: https://youtube.com/playlist?list=PLjl2dJMjkDjmMEptUtRFA1ZMQ9MReTX_f


* <a target="_blank" href="https://www.youtube.com/watch?v=V7ENMLvlzu8">AWS CDK dos and don'ts with Matthew Bonig</a>

https://www.youtube.com/watch?v=3DRiruDUhiA
Using Python to Automate AWS Services | Lambda and EC2

https://medium.com/@rahulsharan512/automating-aws-tasks-with-python-and-boto3-a-step-by-step-guide-1d4c7c93c773

https://medium.com/kpmg-uk-engineering/aws-automation-using-python-and-boto3-1a15b1ffc96b
AWS Automation using python and Boto3 | by Srinath Krishnamoorthy

https://github.com/rahuls512/python-scripts-for-aws
rahuls512/python-scripts-for-aws: Automating AWS Tasks ... - GitHub

https://dev.to/aws-builders/aws-with-python-a-powerful-duo-for-cloud-automation-15a1
AWS with Python: A Powerful Duo for Cloud Automation

https://www.reddit.com/r/devops/comments/wdycmr/how_to_learn_python_for_aws_or_devops_use_cases/
How to learn Python for AWS or DevOps use cases - Reddit

https://aws.amazon.com/blogs/infrastructure-and-automation/category/programing-language/python/
Python | Integration & Automation - AWS
Oct 2, 2019

