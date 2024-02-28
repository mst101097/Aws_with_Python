import boto3

#thorugh using client
'''
client = boto3.client('s3',region_name='us-east-1')

bucket_name = "testmst123"

response = client.delete_bucket(Bucket=bucket_name)

print(f"S3 Bucket{bucket_name} has been deleted")


'''
#Through using resource

resource = boto3.resource('s3',region_name='us-east-1')

bucket_name = "testmst123"

s3_bucket = resource.Bucket(bucket_name)

s3_bucket.delete()

print("This {} bucket has been deleted ".format(bucket_name))

    