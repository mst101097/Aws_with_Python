import boto3

cf_client = boto3.client('cloudformation')

response = cf_client.delete_stack(
    StackName = 'Need to add the stack name here'
)

print(response)