import boto3
from pprint import pprint

ec2_client = boto3.client('ec2')

responese = ec2_client.delete_key_pair(
    KeyName =''
    #here you need to pass the KeyName of ec2 key pair name 
)

pprint(responese)