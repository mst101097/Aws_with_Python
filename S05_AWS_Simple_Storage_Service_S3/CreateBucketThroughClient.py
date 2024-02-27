import boto3

client = boto3.client('s3',region_name='us-east-1')

response = client.create_bucket(
    Bucket = 'testmst123',
    ACL = 'private',

    # If you are using seprate region to create bucket then you need this LocationConstraint declaration
    # CreateBucketConfiguration={
    #     'LocationConstraint':'us-east-1'
    # }        
    
)

print(response)

'''
$ python CreateBucketThroughClient.py
{'ResponseMetadata': {'RequestId': 'BSB8EQ5WRVGGT4V7', ......'Location': '/testmst123'}


'''