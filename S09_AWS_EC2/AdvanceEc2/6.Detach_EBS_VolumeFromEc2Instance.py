import boto3

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

volume = ec2_resource.Volume('vol-0be5c1fce6aedce7c')

print(f"Volume -> {volume.id} Volume state -> {volume.state}")

volume.detach_from_instance(
    Device = '/dev/sdh',
    InstanceId = 'i-00975a838ac4c6356'
)



# vol-06c36f543ce913c68
#using for checking the volume status
waiter = ec2_client.get_waiter('volume_available')
waiter.wait(
    VolumeIds =[
        volume.id
    ]
)
print(f"Volume -> {volume.id} Volume state -> {volume.state}")