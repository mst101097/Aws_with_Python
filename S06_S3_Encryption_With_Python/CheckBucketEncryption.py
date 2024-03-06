import boto3
from botocore.exceptions import ClientError

def checkEncryption():
    s3_client = boto3.client('s3',region_name='us-east-1')

    try:
        response = s3_client.get_bucket_encryption(Bucket="aswmst123")
        print(response)
    except ClientError as e:
        print(e)

checkEncryption()

# {'ResponseMetadata': {'RequestId': 'R9YHEQ1A49V54ZK0', 'HostId': 'H5KERP7I5RJq+8GLuuwlH8f5FDIByZzJdkdw/J6Dln7Qekuptx4pEUA0tAJ4hPxL/ynDmiV4DWAdl73Oi9eUfQ==', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'H5KERP7I5RJq+8GLuuwlH8f5FDIByZzJdkdw/J6Dln7Qekuptx4pEUA0tAJ4hPxL/ynDmiV4DWAdl73Oi9eUfQ==', 'x-amz-request-id': 'R9YHEQ1A49V54ZK0', 'date': 'Wed, 06 Mar 2024 03:34:44 GMT', 'transfer-encoding': 'chunked', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'ServerSideEncryptionConfiguration': {'Rules': [{'ApplyServerSideEncryptionByDefault': {'SSEAlgorithm': 'AES256'}, 'BucketKeyEnabled': False}]}}



# {'ResponseMetadata': {'RequestId': '74G4FVF6AMNHT1DJ', 'HostId': 'HWG7Y0FE2SfdoylaoK2p1aqUbY0NJ1gm4vvmBoboBGE0BXKRHQW1CvqGOBUrA1GasZDvveaTeqCBMQM4yuDBJA==', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'HWG7Y0FE2SfdoylaoK2p1aqUbY0NJ1gm4vvmBoboBGE0BXKRHQW1CvqGOBUrA1GasZDvveaTeqCBMQM4yuDBJA==', 'x-amz-request-id': '74G4FVF6AMNHT1DJ', 'date': 'Wed, 06 Mar 2024 03:37:05 GMT', 'transfer-encoding': 'chunked', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'ServerSideEncryptionConfiguration': {'Rules': [{'ApplyServerSideEncryptionByDefault': {'SSEAlgorithm': 'aws:kms', 'KMSMasterKeyID': 'arn:aws:kms:us-east-1:642678036539:key/80c3b8e0-a737-45b7-954b-ec7111e7bf55'}, 'BucketKeyEnabled': True}]}}

