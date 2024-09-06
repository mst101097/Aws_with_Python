import boto3

ec2_resource = boto3.resource('ec2')

volume = ec2_resource.Volume('vol-0be5c1fce6aedce7c')

print(f"Volume -> {volume.id} Volume state -> {volume.state}")

volume.attach_to_instance(
    Device = '/dev/sdh',
    InstanceId = 'i-00975a838ac4c6356'
)
print(f" EBS attached then  verified the status \n Volume -> {volume.id} Volume state -> {volume.state}")
'''
Volume -> vol-0be5c1fce6aedce7c Volume state -> available
 EBS attached then  verified the status
 Volume -> vol-0be5c1fce6aedce7c Volume state -> in-use

'''