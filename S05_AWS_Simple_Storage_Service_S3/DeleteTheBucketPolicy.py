import boto3


client = boto3.client('s3',region_name='us-east-1')


response = client.delete_bucket_policy(
    Bucket = "awstutorials"
)
print(response)

# delete hosting bucket website

response = client.delete_bucket_website(
    Bucket = "awstutorials"
)
print(response)