import boto3

def detach_usergroup_Policy(group_name,Policy_arn):
    iam = boto3.client('iam')

    response = iam.detach_group_policy(
        GroupName = group_name,
        PolicyArn = Policy_arn
    )

    print(response)

detach_usergroup_Policy('RDSAdmin','arn:aws:iam::aws:policy/AmazonRDSDataFullAccess')
detach_usergroup_Policy('S3Admin','arn:aws:iam::aws:policy/AmazonS3FullAccess')

'''
{'ResponseMetadata': {'RequestId': 'dd33f21b-dd49-45b8-ba6e-c0cd76053dfd', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'dd33f21b-dd49-45b8-ba6e-c0cd76053dfd', 'content-type': 'text/xml', 'content-length': '214', 'date': 'Wed, 13 Dec 2023 12:48:02 GMT'}, 'RetryAttempts': 0}}
{'ResponseMetadata': {'RequestId': 'bf514dd5-a58a-45d8-83e4-c6391004683e', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'bf514dd5-a58a-45d8-83e4-c6391004683e', 'content-type': 'text/xml', 'content-length': '214', 'date': 'Wed, 13 Dec 2023 12:48:03 GMT'}, 'RetryAttempts': 0}}

'''
