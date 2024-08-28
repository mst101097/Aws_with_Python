import boto3

def Terminate_Instances(instanceId):
    ec2_client = boto3.client('ec2')
    response = ec2_client.terminate_instances(InstanceIds=[instanceId])
    print(response)


Terminate_Instances('InstanceID')