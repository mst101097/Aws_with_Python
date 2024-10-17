import boto3
from pprint import pprint

cf_client  = boto3.client('cloudformation')

response = cf_client.get_template(
    StackName = 'need to add the stack name here',
)

# pprint(response)
pprint(response['TemplateBody'])