
"""group.py here.

List Un-used Target Groups.

Based on https://medium.com/kpmg-uk-engineering/aws-automation-using-python-and-boto3-1a15b1ffc96b

"""

import boto3

elbv2Client = boto3.client('elbv2')
response = elbv2Client.describe_target_groups()

unusedTargetGroups = []
for targetGroup in response['TargetGroups']:
    targetGroupARN = targetGroup['TargetGroupArn']
    response = elbv2Client.describe_target_health(TargetGroupArn=targetGroupARN)
    if not response['TargetHealthDescriptions']:
        unusedTargetGroups.append(targetGroupARN)

print(unusedTargetGroups)
