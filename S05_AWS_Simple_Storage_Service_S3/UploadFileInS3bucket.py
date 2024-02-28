import boto3
# Using client upload the file
'''
BUCKET_NAME = "botolession2"

s3_client = boto3.client('s3',region_name='us-east-1')

def upload_files(file_name, bucket,object_name= None,args=None):
    if object_name is None:
        object_name=file_name

    s3_client.upload_file(file_name,bucket,object_name,ExtraArgs=args)
    print("{} has been uploaded to {} bucket".format(file_name,BUCKET_NAME))

upload_files("file.txt",BUCKET_NAME)
'''

# using resource uploading the file

BUCKET_NAME = "botolession2"

s3_resource = boto3.resource('s3',region_name='us-east-1')

def upload_files(file_name, bucket,object_name= None,args=None):
    if object_name is None:
        object_name=file_name

    s3_resource.meta.client.upload_file(file_name,bucket,object_name,ExtraArgs=args)
    print("{} has been uploaded to {} bucket".format(file_name,BUCKET_NAME))

upload_files("file.pdf",BUCKET_NAME)