import boto3

bucket_name = "testmst123"

s3_resource = boto3.resource('s3',region_name='us-east-1')

s3_bucket = s3_resource.Bucket(bucket_name)

def clean_up():

    # delete the objects 
    for s3_objects in s3_bucket.objects.all():
        s3_objects.delete()

    # delete the versioning on objects

    for s3_objects_ver in s3_bucket.object_versions.all():
        s3_objects_ver.delete()

    print("S3 bucket cleaned")


clean_up()

s3_bucket.delete()

print("The Bucket has been deleted ")