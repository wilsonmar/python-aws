
"""ec2-cdk.py here.

List EC2 instances based on tags.

Based on https://medium.com/kpmg-uk-engineering/aws-automation-using-python-and-boto3-1a15b1ffc96b

"""

import boto3

#Declare necessary variables
region = "us-east-1"
instanceNameTagValue = 'No'
instanceIds = []
tag_key = 'Priority'
tag_value = 'No'

#Create EC2 boto3 client
ec2Resource = boto3.resource('ec2', region_name=region)

#Create filter and filter it based on tags "Priority" (Case sensitive)
instances = ec2Resource.instances.filter(
    Filters=[
        {
            'Name': 'tag:Priority',
            'Values': [
                instanceNameTagValue
            ]
        }
    ]
)
print(f'Instances with Tag "Priority={instanceNameTagValue}":')

#List all the EC2 instance with the tag specified
for instance in instances:
    instanceIds.append(instance.id)
print(instanceIds)