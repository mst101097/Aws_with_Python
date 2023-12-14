import boto3

def Delete_myuser(username):
    iam = boto3.client('iam')

    response = iam.delete_user(
        UserName=username
    )

    print(response)

# Delete_myuser('rdsuser')
Delete_myuser('s3user')

'''

{'ResponseMetadata': {'RequestId': '7f0a7296-2d04-406a-9a4a-083630f82200', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '7f0a7296-2d04-406a-9a4a-083630f82200', 'content-type': 'text/xml', 'content-length': '200', 'date': 'Thu, 14 Dec 2023 13:58:59 GMT'}, 'RetryAttempts': 0}}

{'ResponseMetadata': {'RequestId': 'ee8e0e5e-6d22-4ec6-9afa-9f4166019c00', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'ee8e0e5e-6d22-4ec6-9afa-9f4166019c00', 'content-type': 'text/xml', 'content-length': '200', 'date': 'Thu, 14 Dec 2023 14:02:30 GMT'}, 'RetryAttempts': 0}}


'''
