import boto3

def attach_policy(Policy_arn,group_name):
    iam = boto3.client('iam')

    response = iam.attach_group_policy(
        GroupName = group_name,
        PolicyArn = Policy_arn
    )

    print(response)

# attach_policy('arn:aws:iam::aws:policy/AmazonRDSDataFullAccess','RDSAdmin')
'''
{'ResponseMetadata': {'RequestId': 'a68870ee-fe92-41f6-8fff-d161e2b576a4', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'a68870ee-fe92-41f6-8fff-d161e2b576a4', 'content-type': 'text/xml', 'content-length': '214', 'date': 'Wed, 13 Dec 2023 12:19:33 GMT'}, 'RetryAttempts': 0}}
'''
attach_policy('arn:aws:iam::aws:policy/AmazonS3FullAccess','S3Admin')
'''
{'ResponseMetadata': {'RequestId': '60875c89-7bb9-4dff-96e8-192b54b2bc89', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '60875c89-7bb9-4dff-96e8-192b54b2bc89', 'content-type': 'text/xml', 'content-length': '214', 'date': 'Wed, 13 Dec 2023 12:21:59 GMT'}, 'RetryAttempts': 0}}

'''