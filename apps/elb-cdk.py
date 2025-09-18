
"""elb-cdk.py here.

Un-used Transit Gateway and ELB’s.

Based on https://medium.com/kpmg-uk-engineering/aws-automation-using-python-and-boto3-1a15b1ffc96b

"""

import boto3

clientTG = boto3.client('transit-gateway')
clientELB = boto3.client('elbv2')

responseTG = clientTG.describe_transit_gateways()
transitGateways = responseTG['TransitGateways']

responseELB = clientELB.describe_load_balancers()
elbs = responseELB['LoadBalancers']

unusedTransitGateways = []
for tg in transitGateways:
    if tg['Associations'] == [] and tg['Attachments'] == []:
        unusedTransitGateways.append(tg['TransitGatewayId'])

unusedELBs = []
for elb in elbs:
    if elb['AvailabilityZones'] == []:
        unusedELBs.append(elb['LoadBalancerName'])

print(unusedTransitGateways)
print(unusedELBs)

