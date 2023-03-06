from constructs import Construct
from cdktf import App, TerraformStack, S3Backend
from imports.aws.provider import AwsProvider
from imports.aws.iam_role import IamRole
from config import TerraformConfig

DEMO_STACK_ID = 'demo'

class Demo(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        global DEMO_STACK_ID
        tfconfig = TerraformConfig(DEMO_STACK_ID)

        AwsProvider(self, "AWS", 
            region="us-east-2", 
            access_key=tfconfig.provider_access_key,
            secret_key=tfconfig.provider_secret_key,
            token=tfconfig.provider_session_token
        )

        S3Backend(self,
            bucket=tfconfig.backend_bucket,
            key=tfconfig.backend_key,
            encrypt=True,
            region=tfconfig.backend_region,
            dynamodb_table=tfconfig.backend_dynamodb_table
        )

        IamRole(self, 'Role', 
            name='cdk-test',
            assume_role_policy='''
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {
                            "Service": "ec2.amazonaws.com"
                        },
                        "Action": "sts:AssumeRole"
                    }
                ]
            }
            '''
        )
