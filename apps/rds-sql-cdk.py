
"""rds-sql-cdk.py here.

Start and Stop RDS (MySQL, Oracle, etc.).

Based on https://medium.com/kpmg-uk-engineering/aws-automation-using-python-and-boto3-1a15b1ffc96b

"""

import boto3
region = "ap-south-1"
tag_key = 'Priority'
tag_value = 'No'

client = boto3.client('rds', region_name=region)

instances = client.describe_db_instances(Filters=[{'Name': 'tag:' + tag_key, 'Values': [tag_value]}])['DBInstances']

print(f'Instances with Tag "Priority={instanceNameTagValue}":')

for instance in instances:
    instances.start_db_instance(DBInstanceIdentifier=instance['DBInstanceIdentifier'])
    print(f"Started RDS instance {instance['DBInstanceIdentifier']}")
