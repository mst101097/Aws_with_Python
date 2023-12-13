import boto3

def detachPolicy(PolicyARNNumber,username):
    iam = boto3.client('iam')

    response = iam.detach_user_policy(
        UserName = username,
        PolicyArn =PolicyARNNumber )
    
    print(response)


detachPolicy('arn:aws:iam::375253976385:policy/pyFullAccess','testuser1')
'''
{'ResponseMetadata': {'RequestId': 'b6f87367-4d7d-414a-a3af-05cd28db8c67', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'b6f87367-4d7d-414a-a3af-05cd28db8c67', 'content-type': 'text/xml', 'content-length': '212', 'date': 'Mon, 11 Dec 2023 17:17:04 GMT'}, 'RetryAttempts': 0}}

'''