import boto3
from pprint import pprint

ec2_client = boto3.client('ec2')

response  = ec2_client.authorize_security_group_ingress(
    GroupId='sg-00b38ed33da436587',
    IpPermissions=[
        {
            'IpProtocol':'tcp',
            'FromPort':80,
            'ToPort':80,
            'IpRanges':[{'CidrIp':'0.0.0.0/0','Description':'My description'}]
        },
        {
            'IpProtocol':'tcp',
            'FromPort':22,
            'ToPort':22,
            'IpRanges':[{'CidrIp':'0.0.0.0/0','Description':'My description'}]
        }
    ]
)

pprint(response)

'''
{'ResponseMetadata': {'HTTPHeaders': {'cache-control': 'no-cache, no-store',
                                      'content-length': '940',
                                      'content-type': 'text/xml;charset=UTF-8',
                                      'date': 'Wed, 21 Aug 2024 03:15:06 GMT',
                                      'server': 'AmazonEC2',
                                      'strict-transport-security': 'max-age=31536000; '
                                                                   'includeSubDomains',
                                      'x-amzn-requestid': 'dacce53d-0f26-42ed-96ab-f9ccf913c9df'},
                      'HTTPStatusCode': 200,
                      'RequestId': 'dacce53d-0f26-42ed-96ab-f9ccf913c9df',
                      'RetryAttempts': 0},
 'Return': True,
 'SecurityGroupRules': [{'CidrIpv4': '0.0.0.0/0',
                         'Description': 'My description',
                         'FromPort': 80,
                         'GroupId': 'sg-00b38ed33da436587',
                         'GroupOwnerId': '375253976385',
                         'IpProtocol': 'tcp',
                         'IsEgress': False,
                         'SecurityGroupRuleId': 'sgr-0059111dfd48e0622',
                         'ToPort': 80},
                        {'CidrIpv4': '0.0.0.0/0',
                         'Description': 'My description',
                         'FromPort': 22,
                         'GroupId': 'sg-00b38ed33da436587',
                         'GroupOwnerId': '375253976385',
                         'IpProtocol': 'tcp',
                         'IsEgress': False,
                         'SecurityGroupRuleId': 'sgr-09fd3bb0e7c52cd28',
                         'ToPort': 22}]}
'''