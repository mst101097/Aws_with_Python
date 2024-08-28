# import boto3
# from pprint import pprint

# ec2_client = boto3.client('ec2')

# response = ec2_client.delete_security_group(
#     GroupId = 'sg-0802f2224d8e31b90'
#     # passing the group id of security group which one you want to delete.
# )

# pprint(response)


import boto3
import botocore

ec2 = boto3.client('ec2')

try:
    response = ec2.delete_security_group(GroupId='sg-0802f2224d8e31b90')
    print("Security Group Deleted")
except botocore.exceptions.ClientError as e:
    print(f"Error: {e}")
