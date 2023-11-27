import boto3

def create_user(username):
    iam = boto3.client('iam')
    response = iam.create_user(UserName=username)
    print(response)

# create_user('testuser_script')
create_user('testuser_script2')
'''
1. {'User': {'Path': '/', 'UserName': 'testuser_script', 'UserId': 'AIDAVOXXBIVA3ZSEL6BAQ', 'Arn': 'arn:aws:iam::375253976385:user/testuser_script', 'CreateDate': datetime.datetime(2023, 11, 24, 16, 50, 13, tzinfo=tzutc())}, 'ResponseMetadata': {'RequestId': '9547183d-d36b-4ca0-9bc6-cbb88a2557c9', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '9547183d-d36b-4ca0-9bc6-cbb88a2557c9', 'content-type': 'text/xml', 'content-length': '491', 'date': 'Fri, 24 Nov 2023 16:50:12 GMT'}, 'RetryAttempts': 0}}

2 . {'User': {'Path': '/', 'UserName': 'testuser_script2', 'UserId': 'AIDAVOXXBIVA6DTKMM37B', 'Arn': 'arn:aws:iam::375253976385:user/testuser_script2', 'CreateDate': datetime.datetime(2023, 11, 24, 16, 52, 40, tzinfo=tzutc())}, 'ResponseMetadata': {'RequestId': 'ccc0784c-f1d2-4d17-ac7e-c9209ad8cdf3', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'ccc0784c-f1d2-4d17-ac7e-c9209ad8cdf3', 'content-type': 'text/xml', 'content-length': '493', 'date': 'Fri, 24 Nov 2023 16:52:39 GMT'}, 'RetryAttempts': 0}}

'''
