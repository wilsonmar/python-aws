#!/usr/bin/env python3

"""role-iam.py here.

Based on https://learning.oreilly.com/answers2/?questionId=00d8a09c-8d6c-41a7-a838-e4cd72bb74eb

"""

import aws_cdk.aws_iam as iam
from aws_cdk import core. Fn

admin_role = iam.Role(
    self,
    "admin",
    assumed_by=iam.AccountRootPrincipal(Fn.ref("AWS::AccountId"))
)