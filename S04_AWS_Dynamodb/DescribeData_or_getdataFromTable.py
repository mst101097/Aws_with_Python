import boto3
from pprint import pprint

db = boto3.client('dynamodb',region_name='us-east-1')

response = db.describe_table(
    TableName='employee'

)

pprint(response)

'''
Output : 
$ python DescribeData_or_getdataFromTable.py
{'ResponseMetadata': {'HTTPHeaders': {'connection': 'keep-alive',
                                      'content-length': '592',
                                      'content-type': 'application/x-amz-json-1.0',
                                      'date': 'Thu, 15 Feb 2024 04:23:05 GMT',
                                      'server': 'Server',
                                      'x-amz-crc32': '2951715029',
                                      'x-amzn-requestid': 'UIT1VNU4G4T0J3K3AGHABHTSKBVV4KQNSO5AEMVJF66Q9ASUAAJG'},
                      'HTTPStatusCode': 200,
                      'RequestId': 'UIT1VNU4G4T0J3K3AGHABHTSKBVV4KQNSO5AEMVJF66Q9ASUAAJG',
                      'RetryAttempts': 0},
 'Table': {'AttributeDefinitions': [{'AttributeName': 'emp_id',
                                     'AttributeType': 'S'}],
           'CreationDateTime': datetime.datetime(2024, 2, 2, 11, 1, 1, 343000, tzinfo=tzlocal()),
           'DeletionProtectionEnabled': False,
           'ItemCount': 2,
           'KeySchema': [{'AttributeName': 'emp_id', 'KeyType': 'HASH'}],
           'ProvisionedThroughput': {'LastDecreaseDateTime': datetime.datetime(2024, 2, 2, 11, 10, 57, 918000, tzinfo=tzlocal()),
                                     'NumberOfDecreasesToday': 0,
                                     'ReadCapacityUnits': 1,
                                     'WriteCapacityUnits': 1},
           'TableArn': 'arn:aws:dynamodb:us-east-1:642678036539:table/employee',
           'TableClassSummary': {'TableClass': 'STANDARD'},
           'TableId': 'cdf0df15-8c52-40e4-ae40-085d49ceec6c',
           'TableName': 'employee',
           'TableSizeBytes': 39,
           'TableStatus': 'ACTIVE'}}

'''
