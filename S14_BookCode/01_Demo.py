import boto3
# ec2 = boto.connect_ec2(aws_access_key_id='my_access_key',
# aws_secret_access_key='my_secret_key')

ec2 = boto3.client('ec2')
response = ec2.get_all_zones()
print(response)
