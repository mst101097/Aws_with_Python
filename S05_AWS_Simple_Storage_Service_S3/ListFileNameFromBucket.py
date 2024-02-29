import boto3

BUCKET_NAME="botolession2"

s3_resource =  boto3.resource('s3',region_name='us-east-1')

s3_bucket = s3_resource.Bucket(BUCKET_NAME)

print("List of all objects in bucket->\n")

for obj in s3_bucket.objects.all():
    print(obj.key)
    
