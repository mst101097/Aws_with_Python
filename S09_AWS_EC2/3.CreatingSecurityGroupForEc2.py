import boto3
from pprint import pprint

ec2_client = boto3.client('ec2')

response = ec2_client.create_security_group(
    Description ="This is desc",
    GroupName="pygroup",
    VpcId ="vpc-80ccb9fd"
)

pprint(response)

'''
{'GroupId': 'sg-00b38ed33da436587',
 'ResponseMetadata': {'HTTPHeaders': {'cache-control': 'no-cache, no-store',
                                      'content-length': '266',
                                      'content-type': 'text/xml;charset=UTF-8',
                                      'date': 'Wed, 21 Aug 2024 03:05:41 GMT',
                                      'server': 'AmazonEC2',
                                      'strict-transport-security': 'max-age=31536000; '
                                                                   'includeSubDomains',
                                      'x-amzn-requestid': '7829c358-7642-43c4-82da-15138b6bf902'},
                      'HTTPStatusCode': 200,
                      'RequestId': '7829c358-7642-43c4-82da-15138b6bf902',
                      'RetryAttempts': 0}}

'''