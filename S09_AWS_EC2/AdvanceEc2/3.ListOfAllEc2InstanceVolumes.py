import boto3

ec2_resource = boto3.resource('ec2')

for volume in ec2_resource.volumes.all():
    print(volume)

# ec2.Volume(id='vol-0be5c1fce6aedce7c')
# ec2.Volume(id='vol-06c36f543ce913c68')
# ec2.Volume(id='vol-0c04e219701b00180')
