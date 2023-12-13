import boto3
import json

def create_policy():
    iam = boto3.client('iam')

    user_policy ={
    "Version": "2012-10-17",
    "Statement": [
            {
                "Effect": "Allow",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }

    response = iam.create_policy(
        PolicyName = 'pyFullAccess',
        PolicyDocument = json.dumps(user_policy)
    )

    print(response)
create_policy()
'''
{'Policy': {'PolicyName': 'pyFullAccess', 'PolicyId': 'ANPAVOXXBIVASC26DCHQY', 'Arn': 'arn:aws:iam::375253976385:policy/pyFullAccess', 'Path': '/', 'DefaultVersionId': 'v1', 'AttachmentCount': 0, 'PermissionsBoundaryUsageCount': 0, 'IsAttachable': True, 'CreateDate': datetime.datetime(2023, 11, 28, 17, 51, 56, tzinfo=tzutc()), 'UpdateDate': datetime.datetime(2023, 11, 28, 17, 51, 56, tzinfo=tzutc())}, 'ResponseMetadata': {'RequestId': 'b9e0d2b6-936e-466c-bda9-f2a9d1fa8ea7', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'b9e0d2b6-936e-466c-bda9-f2a9d1fa8ea7', 'content-type': 'text/xml', 'content-length': '759', 'date': 'Tue, 28 Nov 2023 17:51:56 GMT'}, 'RetryAttempts': 0}}

'''