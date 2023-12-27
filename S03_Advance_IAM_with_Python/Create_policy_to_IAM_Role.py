import boto3
import json

iam = boto3.client('iam')

policy_name = 'MyNewECPolicy'

policy_document = {
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect":"Allow",
            "Action":"s3:GetObject",
            "Resource":"arn:aws:s3:::01-mstbucketfortest/*"
        }
    ]
}

# arn:aws:s3:::01-mstbucketfortest

iam.create_policy(
    PolicyName=policy_name,
    PolicyDocument = json.dumps(policy_document)
)
print("Policy Created")


