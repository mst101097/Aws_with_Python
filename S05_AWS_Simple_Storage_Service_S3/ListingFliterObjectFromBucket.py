import boto3

BUCKET_NAME="botolession2"

s3_resource = boto3.resource('s3',region_name='us-east-1')

s3_bucket = s3_resource.Bucket(BUCKET_NAME)

print("Listing Filter file name")

for obj in s3_bucket.objects.filter(Prefix="myfile"):
    print(obj.key)

# Listing Filter file name
# myfile.txt
