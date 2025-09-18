
"""secmgr-cdk.py here.

Update Secrets Manager.

Based on https://medium.com/kpmg-uk-engineering/aws-automation-using-python-and-boto3-1a15b1ffc96b

"""

import boto3, json

# declare necessary variables
SecretName = []
AllSecrets = []

secmang = boto3.client('secretsmanager')

# update secrets manager with newly generated access key id and secret key
KeyID = ["key-1","key-2"]
Value = ["value-1","value-2"]
listSecrets = ["secret-a","secret-b"]

for secret in listSecrets:
    OriginalSecret = secmang.get_secret_value(SecretId=secret)
    OriginalSecret = json.loads(OriginalSecret["SecretString"])
    NewSecretValue = {
        KeyID[0]:Value[0],
        KeyID[1]:Value[1]
    }
    OriginalSecret.update(NewSecretValue)
    NewSecretValueStr = json.dumps(OriginalSecret,separators=(',', ':'))
    secmang.update_secret(SecretId=secret,SecretString=NewSecretValueStr)

    