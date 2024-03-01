import boto3

s3 = boto3.resource('s3',region_name='us-east-1')

copy_source ={
    'Bucket':'botolession2',
    'Key':'file.pdf'
}

s3.meta.client.copy(copy_source,'01-mstbucketfortest','copied.pdf')

print("file copied to anouther Bucket..")
