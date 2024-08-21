import boto3
from pprint import pprint

ec2_resource = boto3.resource('ec2')

response = ec2_resource.create_instances(
    ImageId = 'ami-066784287e358dad1',
    MinCount=1,
    MaxCount=1,
    InstanceType ='t2.micro',
    KeyName = 'mykey',
    SecurityGroups=[
        'pygroup'
    ]
)

pprint(response)

# [ec2.Instance(id='i-06750b133bcbdaba9')]
