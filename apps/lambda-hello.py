"""lambda-hello.py here.

https://github.com/wilsonmar/python-aws/blob/master/apps/app.py

Sample code to verify that Lambda functions can be used.

Based on Neoh Gift's 7m AWS CDK 2.8 with Python Deploy Hello World Lambda</a> 2022 (using AWS Cloud9 editor runnig cdk-workshop) at https://learning.oreilly.com/videos/-/01242022VIDEOPAIML

"""

__last_change__ = "25-09-17 v001 + argparse > apps :hello-lambda.py"
__status__ = "Coded. Not tested."

import json

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, CDK! You have hit {}\n'.format(event['path'])
    }
