import boto3
# 'Mypassword@1'

def create_login(username):
    iam = boto3.client('iam')

    login_profile = iam.create_login_profile(
        Password = 'Mypassword@1',
        PasswordResetRequired = False,
        UserName = username
    )

    print(login_profile)

create_login('testuser1')
'''
{'LoginProfile': {'UserName': 'testuser1', 'CreateDate': datetime.datetime(2023, 12, 14, 13, 13, 59, tzinfo=tzutc()), 'PasswordResetRequired': False}, 'ResponseMetadata': {'RequestId': 'd6e17baa-a606-4b5c-8ed4-510c4c5eb8c0', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'd6e17baa-a606-4b5c-8ed4-510c4c5eb8c0', 'content-type': 'text/xml', 'content-length': '462', 'date': 'Thu, 14 Dec 2023 13:13:58 GMT'}, 'RetryAttempts': 0}}

'''
# arn:aws:iam::375253976385:user/testuser1
