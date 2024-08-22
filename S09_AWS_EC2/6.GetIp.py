import boto3
'''
Geting public Ip of instance
'''
def get_Ip(InstanceId):

    ec2_client = boto3.client('ec2')

    reservations = ec2_client.describe_instances(InstanceIds=[InstanceId]).get('Reservations')

    for reservation in reservations:
        for instance in reservation:
            print(instance.get('PublicIpAddress'))

InstanceID = ""
get_Ip(InstanceID)