from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    RemovalPolicy,
    # aws_sqs as sqs,
)
from constructs import Construct
import os

class Sm64CdkDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        website_bucket = s3.Bucket(
            self,
            "sm64Bucket",
            bucket_name="sm64-cdk-demo",
            website_index_document="index.html",
            public_read_access=True,
            block_public_access=s3.BlockPublicAccess(
                block_public_acls=False,
                block_public_policy=False,
                ignore_public_acls=False,
                restrict_public_buckets=False,
            ),
            removal_policy=RemovalPolicy.DESTROY, 
        )

        s3deploy.BucketDeployment(
            self,
            "sm64Deployment",
            sources=[s3deploy.Source.asset(os.path.join("./web"))],
            destination_bucket=website_bucket
        )
