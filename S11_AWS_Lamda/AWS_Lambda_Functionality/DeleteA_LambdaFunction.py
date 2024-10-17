import boto3
from pprint import pprint

lambda_client = boto3.client('lambda')

response = lambda_client.delete_function(
    FunctionName = 'HelloLambdaFunction'
)

pprint(response)

'''
{'ResponseMetadata': {'HTTPHeaders': {'connection': 'keep-alive',
                                      'content-type': 'application/json',
                                      'date': 'Fri, 20 Sep 2024 12:29:40 GMT',
                                      'x-amzn-requestid': '9e41ee83-9d2a-4d2c-8737-9c0161c4e426'},
                      'HTTPStatusCode': 204,
                      'RequestId': '9e41ee83-9d2a-4d2c-8737-9c0161c4e426',
                      'RetryAttempts': 0}}


'''