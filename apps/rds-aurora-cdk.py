
"""rds-aurora-cdk.py here.

List, Start and Stop RDS (Aurora cloud database).

Based on https://medium.com/kpmg-uk-engineering/aws-automation-using-python-and-boto3-1a15b1ffc96b

"""

import boto3

#Declare necessary variables
region = "us-east-1"
tag_key = 'Priority'
tag_value = 'No'
dbIdentifier = []

#Create RDS boto3 Client
client = boto3.client('rds', region_name=region)

#Describe Database instance and filter Database instance details
response = client.describe_db_instances()
instanceDB = response['DBInstances']

#Create a list of the the databases Clusters for Aurora
for i in range(len(instanceDB)):
    dbIdentifier.append(instanceDB[i]['DBClusterIdentifier'])

print(dbIdentifier)

#Based on tag "Priority" start the Aurora RDS cluster
for i in instanceDB:
    tags = dict(i["TagList"][0])
    if tags.get('Key') == 'Priority' and tags.get('Value') =='No':
        client.start_db_cluster(DBClusterIdentifier=i['DBClusterIdentifier'])
