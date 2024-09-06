import boto3

ec2_client = boto3.client('ec2')

volumeID  = 'vol-0be5c1fce6aedce7c'

response = ec2_client.modify_volume(
    VolumeId = volumeID,
    Size = 7
)

print(response)