import boto3

def update_user(old_username, new_username):
    iam = boto3.client('iam')

    response =  iam.update_user(
        UserName = old_username,
        NewUserName = new_username
    )

    print(response)

update_user('testuser_script','testuser1')

'''
{'ResponseMetadata': {'RequestId': 'f0369222-41ba-4b3a-bc6c-17a3bbda6058', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'f0369222-41ba-4b3a-bc6c-17a3bbda6058', 'content-type': 'text/xml', 'content-length': '200', 'date': 'Fri, 24 Nov 2023 17:07:39 GMT'}, 'RetryAttempts': 0}}

'''