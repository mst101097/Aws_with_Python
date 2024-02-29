import boto3

BUCKET_NAME="botolession2"

s3_resource = boto3.resource("s3",region_name='us-east-1')

s3_object =  s3_resource.Object(BUCKET_NAME,'file.pdf')

s3_object.download_file('download.pdf')
print("file is downloaded!!!")
