import boto3

def StopInstances(instanceId):
    ec2_client = boto3.client('ec2')
    response = ec2_client.stop_instances(InstanceIds =[instanceId])

    print(response)

InstanceID  = ""
StopInstances(InstanceID)