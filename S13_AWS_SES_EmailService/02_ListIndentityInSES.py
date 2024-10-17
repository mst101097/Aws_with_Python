import boto3

ses_client = boto3.client('ses')

response = ses_client.list_identities(
    IdentityType = 'EmailAddress'
)

print(response)

'''

{'Identities': ['mca1719214876@gmail.com'], 'ResponseMetadata': {'RequestId': 'f4c1506b-b6d9-4f20-a64f-3f31c3cc1873', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Tue, 08 Oct 2024 10:12:47 GMT', 'content-type': 'text/xml', 'content-length': '340', 'connection': 'keep-alive', 'x-amzn-requestid': 'f4c1506b-b6d9-4f20-a64f-3f31c3cc1873'}, 'RetryAttempts': 0}}


'''
