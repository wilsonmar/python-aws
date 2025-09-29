#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "constructs",
#   "boto3",
#   "psutil",
#   "aws-cdk-lib",
# ]
# ///

"""app.py here.

https://github.com/wilsonmar/python-aws/blob/master/app.py

Use CDK Boto3 SDK to create forever-free services on AWS cloud.
BotoCore takes care of serializing input parameters, signing requests, and deserializing response data into Python dictionaries.
After performing manual steps with an email and credit card to create a master account,
A. authentication logun, with Cognito federation
B. Regions
C. IAM to add users, user keys, roles using 
D. Resource Groups, Resource Explorer https://ocadotechnology.github.io/cmq/
E. Secrets Manager (1$ monthly for each secret), KMS keys, Keyspaces, Keyspaces tables 
F. S3 to create and delete blob objects in buckets
G. Elastic IPs
H. Create and deploy Lambda serverless container images and App Runner = https://github.com/aws-samples/aws-cdk-examples/tree/main/python/url-shortener = create URL Shortener app (because 3rd-party services can become malicious forwarders).
I. VPC networking
J. Monitoring: CloudWatch logs, metrics, alarms, CloudTrail events, 
K. AMIs for ECS to create and drop virtual machines for Host static websites Create RESTful 
L. Use GraphQL APIs to access RDS db with parameter groups (free for 12 months for new AWS customers/accounts. (db.t2.micro, db.t3.micro, db.t4g.micro))
M. Amazon Image Rekognition.
N. Kinesis streams
others.

https://github.com/baxiee/django-cdk-boilerplate with Django for accounts less than a year old:
RDS (postgres, T3 MICRO)
S3 bucket (for static files, images or/and django-admin)
Lambda (DockerImage with 3 MB of memory and 60 second timeout by default)
ECR (keeps only 2 newest images)
API Gateway
RDS secrets (generated automatically)
Other secrets (like DJANGO_SECRET_KEY, generated manually)

Based on coding rules at https://github.com/wilsonmar/python-aws/blob/master/README.md

Drawing from:
* https://docs.aws.amazon.com/code-library/latest/ug/python_3_iam_code_examples.html
* https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iam#code-examples
* https://github.com/namdev-rathod/AWS-CDK
* https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/iam/scenario_create_user_assume_role.py
* https://www.youtube.com/playlist?list=PLO6KswO64zVtwzZyB5G62hjTzinVBBi09  Boto3 basics 2021
* https://www.youtube.com/playlist?list=PLGyRwGktEFqeXUwkqZtiqkMHaz2b_8ojX
* https://github.com/LinkedInLearning/complete-guide-to-serverless-web-app-development-on-aws-4229031
* https://github.com/aws-samples/aws-cdk-examples/tree/main/python#table-of-contents
* https://docs.astral.sh/uv/guides/integration/coiled/#running-scripts-on-the-cloud-with-coiled
IGNORE:
* https://dashbird.io/blog/boto3-aws-python/

USAGE: To run this program, on a Terminal, first:
    ruff check app.py
    uv add aws-cdk-lib constructs boto3 psutil aws_proj.aws_proj_stack --frozen
    # --frozen flag ensures that the exact versions specified in your lock file are used for consistency across environments.

    chmod +x app.py
    uv run app.py -v -vv -s
    cdk deploy '*'

    deactivate   # resources created
        
    # There is not a Python command, but a CLI one, invoked by the subprocess library:
    # https://www.perplexity.ai/search/python-code-to-detect-if-a-str-4W2ynyOgROKIhujPu1u1Hg
    cdk destroy "$my_     # to dispose of the stack.
        # Use --force to avoid the interactive confirmation prompt.
"""

__last_change__ = "25-09-18 v011 + -e .env filepath :app.py"
__status__ = "Passed Ruff. Not tested."


import argparse
from datetime import datetime, timezone
import os
from pathlib import Path
import time
# TODO: logging

try:
    import aws_cdk as cdk         # uv add aws-cdk-lib
    import constructs     # noqa: F401 # uv add constructs   # the foundation of AWS CDK
    import boto3          # noqa: F401 # for Python
    import psutil                # uv add psutil
    from aws_proj.aws_proj_stack import AwsProjStack
    #import aws_cdk.aws_iam as iam
    #from aws_cdk import Fn  #, core
except Exception as e:
    print(f"Python module import failed: {e}")
    # uv run log-time-csv.py
    #print("    sys.prefix      = ", sys.prefix)
    #print("    sys.base_prefix = ", sys.base_prefix)
    print("Please activate your virtual environment:")
    print("   uv vnv .venv\n   source .venv/bin/activate\n   uv add ___\n   uv run app.py")
    exit(9)


# Global variables:
SHOW_VERBOSE = True
SHOW_DEBUG = True
SHOW_SUMMARY = True
loops_count = 0


# For wall time measurements:
pgm_strt_datetimestamp = datetime.now()


def env_variable_load(variable_name, env_file='~/python-samples.env') -> str:
    """Retrieve a variable from a .env file in Python without the external dotenv package.
    
    USAGE: my_variable = env_variable_load('MY_VARIABLE')
    Instead of like: api_key = os.getenv("API_KEY")
    """
    home_path_env = os.path.expanduser('~')+"/python-samples.env"
    # Check for env_file:
    env_path = Path(home_path_env)
    if SHOW_VERBOSE:
        print(f"VERBOSE: env_path={env_path}")
    if env_path.is_file() and env_path.exists():
        if SHOW_DEBUG:
            print("DEBUG: .env file is accessible")
    else:
        print(f"ERROR: .env file {env_path} is not accessible")
        return None

    with open(env_path) as file:
        # FIXME: FileNotFoundError: [Errno 2] No such file or directory: 'Users/johndoe/python-samples.env'
        for line in file:
            # Strip whitespace and ignore comments or empty lines:
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            
            # Split the line into key and value:
            key_value = line.split('=', 1)
            if len(key_value) != 2:
                continue
            
            key, value = key_value
            if key.strip() == variable_name:
                return value.strip().strip('\"').strip('\'')
    return None


#### Time Utility Functions:

def gen_local_timestamp() -> str:
    """Generate a timestamp straing containing the local time with AM/PM & Time zone code."""
    # import pytz
    # now = datetime.now(tz)  # adds time zone.

    # from datetime import datetime
    local_time_obj = datetime.now().astimezone()
    local_timestamp = local_time_obj.strftime("%Y-%m-%d_%I:%M:%S %p %Z%z")  # local timestamp with AM/PM & Time zone codes
    return local_timestamp

def gen_utc_timestamp() -> str:
    """Generate a timestamp straing containing the UTC "Z" time with no AM/PM & Time zone code."""
    # import time
    timestamp = time.time()   # UTC epoch time.
    # from datetime import datetime, timezone
    # Get the current UTC time as a timezone-aware datetime object
    now_utc = datetime.now(timezone.utc)
    # Format the UTC timestamp as a string, e.g., ISO 8601 format
    timestamp = now_utc.strftime('%Y-%m-%dT%H:%M:%SZ')
    return timestamp

## Folders & Files Disk Space Utilities:

def pgm_diskspace_free() -> float:
    """Return the GB of disk space free of the partition in use, using the psutil library."""
    #import os, psutil  #  psutil-5.9.5
    disk = psutil.disk_usage('/')
    free_space_gb = disk.free / (1024 * 1024 * 1024)  # = 1024 * 1024 * 1024
    return free_space_gb

## Memory & Processes Utilities:

def pgm_memory_used() -> (float, str):
    """Return the MiB of RAM for the current process, using the psutil library."""
    #import os, psutil  #  psutil-5.9.5
    process = psutil.Process()
    process_info = str(process)
    mem=process.memory_info().rss / (1024 ** 2)  # in z
    return mem, process_info


#### AWS functions:

# credentials: aws_access_id, aws_secret_access_key, aws_session_token


def role_iam():
    """Add role based on strategic permission design.
    
    See https://learning.oreilly.com/answers2/?questionId=00d8a09c-8d6c-41a7-a838-e4cd72bb74eb
    """
    #import aws_cdk.aws_iam as iam
    #from aws_cdk import core. Fn
    #admin_role = iam.Role(
    #    self,
    #    "admin",
    #   assumed_by=iam.AccountRootPrincipal(Fn.ref("AWS::AccountId"))
    #)


def policies_list():
    """List the managed policies in the AWS account using the AWS SDK for Python (Boto3).

    https://docs.aws.amazon.com/code-library/latest/ug/python_3_iam_code_examples.html
    """
    iam = boto3.client("iam")
    try:
        # Get a paginator for the list_policies operation:
        paginator = iam.get_paginator("list_policies")
        # Iterate through the pages of results:
        for page in paginator.paginate(Scope="All", OnlyAttached=False):
            for policy in page["Policies"]:
                print(f"Policy name: {policy['PolicyName']}")
                print(f"Policy  ARN: {policy['Arn']}")
    except boto3.exceptions.BotoCoreError as e:
        print(f"iam_hello() boto3.exceptions.BotoCoreError: {e}")



# s3 buckets list: https://www.youtube.com/watch?v=ZR6adef3fCM
# https://github.com/franchyze923/Code_From_Tutorials

 
def aws-secrets-rotator():
    """Rotate API keys automatically without manual updates."""
    # import boto3, requests
    client = boto3.client('secretsmanager')
    def rotate_secret(secret_name):
        new_key = requests.post("https://api.random.org/api-key").text
        client.put_secret_value(SecretId=secret_name, SecretString=new_key)

def chaos-monkey-instance():
    """Create spot instance of Chaos Monkey.

    Bid on cheap spot instances and survive interruptions.
    """
    # import boto3
    ec2 = boto3.client('ec2')
    def launch_spot():
        ec2.request_spot_instances(
            SpotPrice='0.01',
            InstanceCount=1,
            LaunchSpecification={
                'ImageId':'ami-xxxxxx',
                'InstanceType':'t3.micro'
            })

#### Summary

def pgm_summary(std_strt_datetimestamp, loops_count):
    """Print summary count of files processed and the time to do them."""
    # For wall time of standard imports:
    pgm_stop_datetimestamp = datetime.now()
    pgm_elapsed_wall_time = pgm_stop_datetimestamp - pgm_strt_datetimestamp

    if SHOW_SUMMARY:
        pgm_stop_mem_used, process_data = pgm_memory_used()
        pgm_stop_mem_diff = pgm_stop_mem_used - pgm_strt_mem_used
        print(f"{pgm_stop_mem_diff:.6f} MB memory consumed during run in {process_data}.")

        pgm_stop_disk_diff = pgm_strt_disk_free - pgm_diskspace_free()
        print(f"{pgm_stop_disk_diff:.6f} GB disk space consumed during run.")

        print(f"SUMMARY: Ended while attempting loop {loops_count} in {pgm_elapsed_wall_time} seconds.")
    else:
        print(f"SUMMARY: Ended while attempting loop {loops_count}.")


#### SECTION 07 - Read custom command line (CLI) arguments controlling this program run:


parser = argparse.ArgumentParser(description="gcp-services.py for Google Cloud Authentication")
#parser.add_argument("-h", "--help", action="store_true", help="Help (this menu)")
parser.add_argument("-q", "--quiet", action="store_true", help=" Withhold INFO, ERROR, FATAL, summary messages.")
parser.add_argument("-s", "--summary", action="store_true", help="Show run statistics at beginning and end of run")
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose: show internal data")
parser.add_argument("-vv", "--debug", action="store_true", help="Show debugging data")
parser.add_argument("-l", "--log", action="store_true", help="Log events to a telemetry system.")
parser.add_argument("-a", "--alert", action="store_true", help="Send alerts (used during productive runs).")

parser.add_argument("-e", "--env", type=str, required=False, help="path to .env file containing configs &secrets (API keys).")
parser.add_argument("-D", "--destroy", action="store_true", help="Destroy resources at end of run.")

# Load arguments from CLI:
args = parser.parse_args()


#### SECTION 08 - Override defaults and .env file with run-time parms:

# Defaults:
SHOW_QUIET = False
SHOW_VERBOSE = False
SHOW_DEBUG = False
SHOW_SUMMARY = False
send_alert = False
destroy_resc = False

if args.verbose:         # -v --verbose (flag)
    SHOW_VERBOSE = True
if args.debug:           # -vv --debug (flag)
    SHOW_DEBUG = True
if args.summary:         # -s --summary (flag)
    SHOW_SUMMARY = True
# After individual ones above:
if args.quiet:           # -q --quiet
    SHOW_VERBOSE = False
    SHOW_DEBUG = False
    SHOW_SUMMARY = False

if args.alert:           # -a  --alert
    send_alert = True
if args.log:             # -L  --log
    log_events = True
if args.env:             # -e  --env file-path
    env_path = args.env
if args.destroy:         # -D  --destroy
    destroy_resc = True




if __name__ == '__main__':

    local_timestamp = gen_local_timestamp()
    loops_count =+ 1

    pgm_strt_mem_used, pgm_process = pgm_memory_used()
    pgm_strt_disk_free = pgm_diskspace_free()
    if SHOW_DEBUG:
        print(f"app.py started: {pgm_strt_datetimestamp}")
        print(f"DEBUG: {pgm_process}")
        print("DEBUG: pgm_memory used()="+str(pgm_strt_mem_used)+" MiB being used.")
        print(f"DEBUG: pgm_diskspace_free()={pgm_strt_disk_free:.2f} GB")
        # list_disk_space_by_device()

    app = cdk.App()
    AwsProjStack(app, "AwsProjStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html

    policies_list()   # hello_iam

    )

    # Boto3 is a runtime AWS service that interacts with AWS directly—calling S3.create_bucket() or EC2.run_instances() to provision resources instantly, not via templates.

    # app.synth() is the final "build" step for your resource stack — to output your intended infrastructure, separate from direct resource API calls.

    # app.synth() collects synthesizes constructs, stacks, and resources for outputs to CloudFormation templates and assets for later deployment - stacks to CloudFormation templates:
    # See https://docs.aws.amazon.com/cdk/v2/guide/configure-synth.html
    app.synth()
    # This generate CloudFormation templates from your app constructs.

    if destroy_resc:
        print("-D destroy_resc() here.")

    if SHOW_SUMMARY:
        pgm_summary(pgm_strt_datetimestamp, loops_count)

"""
$ uv run app.py
app.py started: 2025-09-16 19:06:18.153274
DEBUG: psutil.Process(pid=13849, name='Python', status='running', started='19:06:15')
DEBUG: pgm_memory used()=414.84375 MiB being used.
DEBUG: pgm_diskspace_free()=368.20 GB
0.046875 MB memory consumed during run in psutil.Process(pid=13849, name='Python', status='running', started='19:06:15').
0.000042 GB disk space consumed during run.
SUMMARY: Ended while attempting loop 0 in 0:00:00.092067 seconds.
"""