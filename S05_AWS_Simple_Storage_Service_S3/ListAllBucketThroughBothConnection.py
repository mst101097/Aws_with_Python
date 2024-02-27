import boto3

'''
#Fetching bucket Through client
client= boto3.client('s3',region_name='us-east-1')

response = client.list_buckets()

print("List of Bucket..")

for bucket in response['Buckets']:
    print(bucket['Name'])

'''
#Fetcging through resource connection
resource =  boto3.resource('s3',region_name='us-east-1')

itertor = resource.buckets.all()

print("Lists of Bucket")

for bucket in itertor:
    print(bucket.name)

'''
Lists of Bucket
01-mstbucketfortest
botolession2
testmst123

'''