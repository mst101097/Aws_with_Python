import boto3
import boto3.resources

# it is through ec2 client  connections
'''
ec2_client = boto3.client('ec2')

new_volume = ec2_client.create_volume(
    AvailabilityZone  = 'us-east-1a',
    Size = 5,
    VolumeType = 'gp2',
    TagSpecifications = [
        {
            'ResourceType' : 'volume',
            'Tags' : [
                {
                    'Key' : 'Name',
                    'Value' : 'Python & Boto3'
                }
            ]
        }
    ] 
)

print(f"Volume Created {new_volume['VolumeId']}")


# Unknown parameter in input: "TagsSpecifications", must be one of: AvailabilityZone, Encrypted, Iops, KmsKeyId, OutpostArn, Size, SnapshotId, VolumeType, DryRun, TagSpecifications, MultiAttachEnabled, Throughput, ClientToken

# Volume Created vol-0c04e219701b00180

'''

# it is through the ec2_resource connection

ec2_resource = boto3.resource('ec2')

new_volume = ec2_resource.create_volume(
    AvailabilityZone  = 'us-east-1a',
    Size = 5,
    VolumeType = 'gp2',
    TagSpecifications = [
        {
            'ResourceType' : 'volume',
            'Tags' : [
                {
                    'Key' : 'Name',
                    'Value' : 'Python & Boto3 with resource'
                }
            ]
        }
    ] 
)

print(f"Volume Created {new_volume.id}")

# Volume Created vol-0be5c1fce6aedce7c
