import json
import boto3

s3 = boto3.resource('s3')



def lambda_handler(event, context):
    # TODO implement
    s3_buckets = []
    for bucket in s3.buckets.all():
        s3_buckets.append(bucket.name)
    return {
        'statusCode': 200,
        'body': s3_buckets 
    }
