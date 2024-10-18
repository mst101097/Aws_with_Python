import boto3
from pprint import pprint

ses_client = boto3.client('ses')

response = ses_client.send_templated_email(
    Source ='mca1719214876@gmail.com',
    Destination ={
        'ToAddresses':['mca1719214876@gmail.com']
    },
    ReplyToAddresses = [],
    Template = 'CustomTemplate',
    TemplateData = '{"replace":"value"}'
)

print(response)

# {'MessageId': '010001929a0c666e-2dd06675-12b5-4353-b82e-f154f83dab64-000000', 'ResponseMetadata': {'RequestId': '6c761bef-6cf1-4bc2-b678-90532c0d816e', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Thu, 17 Oct 2024 10:35:56 GMT', 'content-type': 'text/xml', 'content-length': '362', 'connection': 'keep-alive', 'x-amzn-requestid': '6c761bef-6cf1-4bc2-b678-90532c0d816e'}, 'RetryAttempts': 0}}
