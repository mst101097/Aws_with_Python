import boto3

from pprint import pprint

client = boto3.client('s3',region_name='us-east-1')

response = client.get_bukcet_website(
    Bucket=""
)
pprint(response)