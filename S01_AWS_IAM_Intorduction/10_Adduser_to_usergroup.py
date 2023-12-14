import boto3

def add_user(username, group_name):
    iam = boto3.client('iam')

    response = iam.add_user_to_group(
        UserName=username,
        GroupName=group_name

    )
    print(response)

add_user('rdsuser','RDSAdmin')
add_user('s3user','S3Admin')
'''
{'ResponseMetadata': {'RequestId': '4027b08f-2a4f-4a72-a8ca-936bc53a0ad3', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '4027b08f-2a4f-4a72-a8ca-936bc53a0ad3', 'content-type': 'text/xml', 'content-length': '208', 'date': 'Wed, 13 Dec 2023 12:35:23 GMT'}, 'RetryAttempts': 0}}
{'ResponseMetadata': {'RequestId': '911e393c-6275-4654-92c7-9af25630d348', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '911e393c-6275-4654-92c7-9af25630d348', 'content-type': 'text/xml', 'content-length': '208', 'date': 'Wed, 13 Dec 2023 12:35:24 GMT'}, 'RetryAttempts': 0}}

'''