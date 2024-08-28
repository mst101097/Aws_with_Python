import boto3

ec2 = boto3.resource('ec2')

# Replace with your security group ID
security_group_id = 'sg-0802f2224d8e31b90'

# Find EC2 instances using the security group
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance.group-id', 'Values': [security_group_id]}])

for instance in instances:
    print(f"Instance {instance.id} is using the security group {security_group_id}")

# Then detach or modify these instances before deleting the security group
