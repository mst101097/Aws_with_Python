import boto3

db = boto3.client('dynamodb',region_name='us-east-1')

response = db.get_item(
    TableName = 'employee',
    Key={
        'emp_id':{
            'S':'5'
        }
    }
)
print(response)

'''
{'Item': {'name': {'S': 'test5'}, 'age': {'S': '30'}, 'emp_id': {'S': '5'}}, 'ResponseMetadata': {'RequestId': 'NF84P2FULH7GD7FEPI59LEA7CFVV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'Server', 'date': 'Tue, 20 Feb 2024 03:07:17 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '67', 'connection': 'keep-alive', 'x-amzn-requestid': 'NF84P2FULH7GD7FEPI59LEA7CFVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '2750675798'}, 'RetryAttempts': 0}}

'''