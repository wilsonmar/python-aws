
"""sg-cdk.py here.

List un-used Security Group across all regions.

This needs to run so they can be taken advantage of by malicious bots.

Based on https://medium.com/kpmg-uk-engineering/aws-automation-using-python-and-boto3-1a15b1ffc96b

"""

import json
import boto3

client = boto3.client('ec2')
regions_dict = client.describe_regions()
region_list = [region['RegionName'] for region in regions_dict['Regions']]

def unused_securitygroups():
    for region in region_list:
        
        ec2 = boto3.resource('ec2', region_name=region) #region
        client = boto3.client('ec2', region_name=region) #region
        
        sgs = list(ec2.security_groups.all())
        
        #All Security groups without default because you cant delete default one
        all_sgs = set([sg.group_id for sg in sgs if sg.group_name != 'default'])
       
        #All Security Groups that are attached to EC2 and NetworkInterfaces
        response = client.describe_network_interfaces()
        attachedSecGroupIDs = []
        for i in response["NetworkInterfaces"]:
        #Check if the security group is attached
        
            if 'Attachment' in i and i['Attachment']['Status'] == 'attached':
                #Create a set with the attached SGs
                attachedSecGroupIDs += [g['GroupId'] for g in i['Groups']]
        
        unused_sgs = all_sgs - set(attachedSecGroupIDs)
        
        for id in list(unused_sgs):
            unused_sec_grp = ec2.SecurityGroup(id)
            print(region +": "+id)
            #unused_sec_grp.delete()    
            
unused_securitygroups()
