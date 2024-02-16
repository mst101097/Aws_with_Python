# update and change the table in Dynamodb
import boto3

db = boto3.client('dynamodb',region_name='us-east-1')

response =  db.update_table(
    TableName='employee',
    BillingMode='PROVISIONED',

    ProvisionedThroughput={
        'ReadCapacityUnits':1,
        'WriteCapacityUnits':1
    }
)

print(response)

'''
{'TableDescription': {'AttributeDefinitions': [{'AttributeName': 'emp_id', 'AttributeType': 'S'}], 'TableName': 'employee', 'KeySchema': [{'AttributeName': 'emp_id', 'KeyType': 'HASH'}], 'TableStatus': 'UPDATING', 'CreationDateTime': datetime.datetime(2024, 2, 2, 11, 1, 1, 343000, tzinfo=tzlocal()), 'ProvisionedThroughput': {'LastIncreaseDateTime': datetime.datetime(2024, 2, 16, 9, 6, 35, 370000, tzinfo=tzlocal()), 'LastDecreaseDateTime': datetime.datetime(2024, 2, 2, 11, 10, 57, 918000, tzinfo=tzlocal()), 'NumberOfDecreasesToday': 0, 'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}, 'TableSizeBytes': 125, 'ItemCount': 6, 'TableArn': 'arn:aws:dynamodb:us-east-1:642678036539:table/employee', 'TableId': 'cdf0df15-8c52-40e4-ae40-085d49ceec6c', 'TableClassSummary': {'TableClass': 'STANDARD'}, 'DeletionProtectionEnabled': False}, 'ResponseMetadata': {'RequestId': 'RC2DJKP01M2SSUVV5USEC4SBDBVV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'Server', 'date': 'Fri, 16 Feb 2024 03:36:35 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '645', 'connection': 'keep-alive', 'x-amzn-requestid': 'RC2DJKP01M2SSUVV5USEC4SBDBVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '1045598808'}, 'RetryAttempts': 0}}

Now set the previous value 1
'''