import boto3

ec2_resource = boto3.resource('ec2')

volumeid = ""

# vol-0c04e219701b00180

snapshot = ec2_resource.create_snapshot(
    VolumeId = volumeid,
    TagSpecifications =[
        {
            'ResourceType':'snapshot',
            'Tags':[
                {
                    'Key':'Name',
                    'Value':'Python Snapshot'
                }
            ]
        }
    ]
)

print("Snapshot created.........")