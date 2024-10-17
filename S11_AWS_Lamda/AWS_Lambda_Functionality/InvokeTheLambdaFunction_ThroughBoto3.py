import boto3
import json

lambda_client = boto3.client('lambda')

test_event = {}

response = lambda_client.invoke(
    FunctionName = 'HelloLambdaFunction',
    Payload = json.dumps(test_event)
)

print(response['Payload'])
print(response['Payload'].read().decode('utf-8'))

'''

<botocore.response.StreamingBody object at 0x000002294C781C90>
{"statusCode": 200, "body": "\"Hello From Python & boto3\""}

'''