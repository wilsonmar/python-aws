
"""ebs-cdk.py here.

List Un-encrypted and gp2 EBS Volumes.

Based on https://medium.com/kpmg-uk-engineering/aws-automation-using-python-and-boto3-1a15b1ffc96b

"""

import boto3

region = "us-east-1"
ec2Resource = boto3.resource('ec2', region_name=region)
client = boto3.client('ec2')
response = client.describe_volumes()["Volumes"]

ebsVolumeID = []
ebsState = []
ebsType = []
ebsEncrypted = []
output1 = [] # unencrypted attached EBS Volume
output2 = [] # attached gp2 ebs volumes

for i in range(len(response)):
    ebsVolumeID.append(response[i]["VolumeId"])
    ebsState.append(response[i]["State"])
    ebsType.append(response[i]["VolumeType"])
    ebsEncrypted.append(response[i]["Encrypted"])

for i in range(len(response)):
    if ebsState[i] == "attached" and ebsEncrypted[i] == True:
        output1.append(ebsVolumeID[i])
    if ebsState[i] == "attached" and ebsType[i] == "gp2":
        output2.append(ebsVolumeID[i])

print(output1,output2)

