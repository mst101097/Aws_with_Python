import boto3

s3 = boto3.resource('s3',region_name='us-east-1')

BUCKET_NAME="botolession2"

objectsummary = s3.ObjectSummary(BUCKET_NAME,'myfile.txt')

print("bucketName -",objectsummary.bucket_name)
print('ObjectName ->',objectsummary.key)


