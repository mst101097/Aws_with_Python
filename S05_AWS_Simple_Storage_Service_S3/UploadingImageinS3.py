import boto3

client= boto3.client('s3',region_name='us-east-1')


with open('awsimage.png','rb')as f:
    data=f.read()

response = client.put_object(
    ACL="private",
    Bucket="testmst123",
    Body= data,
    Key='awsimage.png'
)

print(response)


'''
{'ResponseMetadata': {'RequestId': 'K4K5CYCAQG669E8S', ....'ServerSideEncryption': 'AES256'}
'''