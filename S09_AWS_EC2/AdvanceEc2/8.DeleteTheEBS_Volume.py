import boto3

ec2_resource = boto3.resource('ec2')

# vol-0c04e219701b00180
# vol-0be5c1fce6aedce7c
volume = ec2_resource.Volume('vol-0c04e219701b00180')

if volume.state == "available":
    volume.delete()
    print("Volume Delete..")
else:
    print("You can not delete the volume")