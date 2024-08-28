import boto3
from pprint import pprint

user_data ="""
#!/bin/bash
yum update -y 
yum install -y httpd
chkconfig httpd on
service httpd start
echo "<h1>Welcome to Python & Boto3 Course</h1>" > /var/www/html/index.html
"""
ec2_resource = boto3.resource('ec2')


response = ec2_resource.create_instances(
    ImageId ='ami-066784287e358dad1',
    MinCount = 1,
    MaxCount = 1,
    InstanceType='t2.micro',
    KeyName ='Django',
    SecurityGroups=[
        'pygroup'
    ],
    UserData = user_data
)

pprint(response)
# [ec2.Instance(id='i-00975a838ac4c6356')]
