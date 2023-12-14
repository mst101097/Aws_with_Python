import boto3
'''
def create_accessKey_for_User(username):
    iam = boto3.client('iam')

    response = iam.create_access_key(
        UserName=username
    )

    print(response)

create_accessKey_for_User('rdsuser')

# {'AccessKey': {'UserName': 'rdsuser', 'AccessKeyId': 'AKIAVOXXBIVAYE2QLL2I', 'Status': 'Active', 'SecretAccessKey': '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', 'CreateDate': datetime.datetime(2023, 12, 14, 12, 50, 3, tzinfo=tzutc())}, 'ResponseMetadata': {'RequestId': '944eff7b-050a-49ef-968d-a829c5f53d4c', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '944eff7b-050a-49ef-968d-a829c5f53d4c', 'content-type': 'text/xml', 'content-length': '549', 'date': 'Thu, 14 Dec 2023 12:50:02 GMT'}, 'RetryAttempts': 0}}

'''

def Update_accessKey():
    iam  = boto3.client('iam')
    response = iam.update_access_key(
        AccessKeyId = 'AKIAVOXXBIVAYE2QLL2I',
        Status = 'Inactive',
        UserName='rdsuser'
    )

    print(response)

Update_accessKey()
'''
{'ResponseMetadata': {'RequestId': '7f63bac5-a80f-4ab6-b409-c1c4d4535f6a', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '7f63bac5-a80f-4ab6-b409-c1c4d4535f6a', 'content-type': 'text/xml', 'content-length': '210', 'date': 'Thu, 14 Dec 2023 12:59:17 GMT'}, 'RetryAttempts': 0}}

'''