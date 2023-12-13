import boto3

def attach_policy(policy_ARN,username):
    iam = boto3.client('iam')

    response =  iam.attach_user_policy(
        UserName = username,
        PolicyArn  = policy_ARN
    )

    print(response)

# attach_policy('arn:aws:iam::375253976385:policy/pyFullAccess','testuser1')
'''
{'ResponseMetadata': {'RequestId': '1452e87b-a890-4b63-aa2c-5ac74f3c85d3', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '1452e87b-a890-4b63-aa2c-5ac74f3c85d3', 'content-type': 'text/xml', 'content-length': '212', 'date': 'Mon, 11 Dec 2023 15:02:09 GMT'}, 'RetryAttempts': 0}}

'''


attach_policy('arn:aws:iam::aws:policy/AmazonRDSFullAccess','testuser_script2')
'''
{'ResponseMetadata': {'RequestId': '418b4836-9f12-4b28-b8e3-662e1a4dc778', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '418b4836-9f12-4b28-b8e3-662e1a4dc778', 'content-type': 'text/xml', 'content-length': '212', 'date': 'Mon, 11 Dec 2023 15:06:56 GMT'}, 'RetryAttempts': 0}}


'''