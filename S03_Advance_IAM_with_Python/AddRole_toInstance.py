import boto3


iam = boto3.client('iam')

role_name ="MyNewEC2Role"

instance_profile_name = "MyNewEC2Profile"

response = iam.add_role_to_instance_profile(
    InstanceProfileName = instance_profile_name,
    RoleName = role_name

)

print(response)
'''
{'ResponseMetadata': {'RequestId': 'c87ef491-7cd3-4d80-92e2-f4a79429b6d2', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'c87ef491-7cd3-4d80-92e2-f4a79429b6d2', 'content-type': 'text/xml', 'content-length': '228', 'date': 'Tue, 02 Jan 2024 14:31:41 GMT'}, 'RetryAttempts': 0}}

'''