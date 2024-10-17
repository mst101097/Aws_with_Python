import boto3
from pprint import pprint
cf_client = boto3.client('cloudformation')
# cf_resource = boto3.resource('cloudformation')

with open('DynamoDB.yml', 'r') as f: 
    dy_template = f.read()
    # print(dy_template)


params = [
    {
        'ParameterKey' : 'HashKeyElementName',
        'ParameterValue' : 'EmployeeId'
    }
]

response = cf_client.create_stack(
    StackName  = 'dynamostack',
    TemplateBody = dy_template,
    Parameters = params
)

pprint(response)

'''
{'ResponseMetadata': {'HTTPHeaders': {'connection': 'keep-alive',
                                      'content-length': '381',
                                      'content-type': 'text/xml',
                                      'date': 'Mon, 07 Oct 2024 09:55:39 GMT',
                                      'x-amzn-requestid': 'd037333e-1fd6-4046-9bc7-1e5249c121a0'},
                      'HTTPStatusCode': 200,
                      'RequestId': 'd037333e-1fd6-4046-9bc7-1e5249c121a0',
                      'RetryAttempts': 0},
 'StackId': 'arn:aws:cloudformation:us-east-1:375253976385:stack/dynamostack/4ec91f70-8492-11ef-a8f1-12969a89f1bf'}

'''