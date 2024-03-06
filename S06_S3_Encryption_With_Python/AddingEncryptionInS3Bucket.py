import boto3

def set_encryption():
    s3_client = boto3.client('s3',region_name='us-east-1')

    response = s3_client.put_bucket_encryption(
        Bucket = "aswmst123",
        ServerSideEncryptionConfiguration={
            "Rules":[
                {"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm":"AES256"}}
            ]
        }
    )
    print(response)

set_encryption()

# {'ResponseMetadata': {'RequestId': '466XB44RW8RMPB46', 'HostId': 'a0evJUrdpOSALj0WDX4r1NiZFG/TjBRaGiecR1NTQSjfS3MS5K1pmPXdzyofQTAFhyYgegUNk0xI+5GcoHCScpsvDThz0lwwX3bSNL09rnY=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'a0evJUrdpOSALj0WDX4r1NiZFG/TjBRaGiecR1NTQSjfS3MS5K1pmPXdzyofQTAFhyYgegUNk0xI+5GcoHCScpsvDThz0lwwX3bSNL09rnY=', 'x-amz-request-id': '466XB44RW8RMPB46', 'date': 'Wed, 06 Mar 2024 03:27:29 GMT', 'server': 'AmazonS3', 'content-length': '0'}, 'RetryAttempts': 0}}

