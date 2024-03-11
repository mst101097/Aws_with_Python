import boto3

bucket_name='aswmst123'
def delete_encryption():
    s3_client = boto3.client('s3',region_name='us-east-1')
    response = s3_client.delete_bucket_encryption(Bucket=bucket_name)
    print(response)

delete_encryption()

# {'ResponseMetadata': {'RequestId': 'EG3JE0XS5RBB2YC7', 'HostId': 'bDve3G/1XcXQoSX4bB2BlD2YpoLiK8Epc16jyGzEny6PQsZRkMBoWdLVWxoKW13XDC8SyoGtmU0=', 'HTTPStatusCode': 204, 'HTTPHeaders': {'x-amz-id-2': 'bDve3G/1XcXQoSX4bB2BlD2YpoLiK8Epc16jyGzEny6PQsZRkMBoWdLVWxoKW13XDC8SyoGtmU0=', 'x-amz-request-id': 'EG3JE0XS5RBB2YC7', 'date': 'Mon, 11 Mar 2024 03:38:41 GMT', 'server': 'AmazonS3'}, 'RetryAttempts': 0}}
