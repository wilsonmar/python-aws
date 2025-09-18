
"""iam-key-rotate-cdk.py here.

Rotate IAM Access Keys.

Based on https://medium.com/kpmg-uk-engineering/aws-automation-using-python-and-boto3-1a15b1ffc96b

"""

import boto3, json
from datetime import datetime, timezone

# declare necessary variables
RegionName = 'eu-west-1'
MaxKeyAge = 90
ExpiredAccessKeyID = []
ExpiredAccessKeyUser = []

# establish a client connection
iam = boto3.client('iam', region_name=RegionName)

paginator = iam.get_paginator('list_users')
CurrentDate = datetime.now(timezone.utc)

# List all the expired Access Keys whose age is > 90 days
for response in paginator.paginate():
    for user in response['Users']:
        UserName = user['UserName']
        ListKey = iam.list_access_keys(UserName=UserName)
        for AccessKey in ListKey['AccessKeyMetadata']:
            AccessKeyId = AccessKey['AccessKeyId']
            KeyCreationDate = AccessKey['CreateDate']
            age = (CurrentDate - KeyCreationDate).days
            if age <= MaxKeyAge:
                ExpiredAccessKeyID.append(AccessKeyId)
                ExpiredAccessKeyUser.append(UserName)
print(ExpiredAccessKeyID, ExpiredAccessKeyUser)

# created a new access keys for all the users who's access keys are disabled
NewAppKeyID = []
NewAppSecretsKey = []

for user in ExpiredAccessKeyUser:
    if user==<your-user>:
        responseApp = iam.create_access_key(UserName=user)
        NewAppKeyID.append(responseApp["AccessKey"]["AccessKeyId"])
        NewAppSecretsKey.append(responseApp["AccessKey"]["SecretAccessKey"])
        
#delete the access keys who's age is > 90 days
for key1, key2 in zip(ExpiredAccessKeyID, ExpiredAccessKeyUser):
    if key2 == <your-user>:
        iam.update_access_key(AccessKeyId=key1, UserName=key2, Status='Inactive')
        iam.delete_access_key(AccessKeyId=key1, UserName=key2)

