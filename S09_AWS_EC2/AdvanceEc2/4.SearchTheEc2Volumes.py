import boto3

ec2_resource = boto3.resource('ec2')

for volume in ec2_resource.volumes.filter(
    Filters = [
        {
            'Name' : 'tag:Name',
            'Values' : [ 'Python & Boto3 with resource',
            ]
        }
    ]
):
    print(f' Volume ID ->  {volume.id} volume -> {volume.size} gib -> {volume.state}')
#  Volume ID ->  vol-0be5c1fce6aedce7c volume -> 5 gib -> available
