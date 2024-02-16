# in this file we using crreate and delete table backup

import boto3

db = boto3.client('dynamodb',region_name='us-east-1')

'''
# creating backup for employee table
response = db.create_backup(
    TableName='employee',
    BackupName='employeeBackup'
)

print(response)

{'BackupDetails': {'BackupArn': 'arn:aws:dynamodb:us-east-1:642678036539:table/employee/backup/01708055245570-cf505fc0', 'BackupName': 'employeeBackup', 'BackupSizeBytes': 125, 'BackupStatus': 'CREATING', 'BackupType': 'USER', 'BackupCreationDateTime': datetime.datetime(2024, 2, 16, 9, 17, 25, 570000, tzinfo=tzlocal())}, 'ResponseMetadata': {'RequestId': '20MS9UF8ITPQFL5KK3GMSGRM8FVV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'Server', 'date': 'Fri, 16 Feb 2024 03:47:25 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '258', 'connection': 'keep-alive', 'x-amzn-requestid': '20MS9UF8ITPQFL5KK3GMSGRM8FVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '268030237'}, 'RetryAttempts': 0}}
'''
# deleteing backup for employee table

response = db.delete_backup(
    BackupArn='arn:aws:dynamodb:us-east-1:642678036539:table/employee/backup/01708055245570-cf505fc0'
)

print(response)
'''
'BackupDescription': {'BackupDetails': {'BackupArn': 'arn:aws:dynamodb:us-east-1:642678036539:table/employee/backup/01708055245570-cf505fc0', 'BackupName': 'employeeBackup', 'BackupSizeBytes': 125, 'BackupStatus': 'DELETED', 'BackupType': 'USER', 'BackupCreationDateTime': datetime.datetime(2024, 2, 16, 9, 17, 25, 570000, tzinfo=tzlocal())}, 'SourceTableDetails': {'TableName': 'employee', 'TableId': 'cdf0df15-8c52-40e4-ae40-085d49ceec6c', 'TableArn': 'arn:aws:dynamodb:us-east-1:642678036539:table/employee', 'TableSizeBytes': 125, 'KeySchema': [{'AttributeName': 'emp_id', 'KeyType': 'HASH'}], 'TableCreationDateTime': datetime.datetime(2024, 2, 2, 11, 1, 1, 343000, tzinfo=tzlocal()), 'ProvisionedThroughput': {'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}, 'ItemCount': 6, 'BillingMode': 'PROVISIONED'}, 'SourceTableFeatureDetails': {}}, 'ResponseMetadata': {'RequestId': 'KF9PTCP6V0R4IACB6BSIOF4J7BVV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'Server', 'date': 'Fri, 16 Feb 2024 03:52:49 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '706', 'connection': 'keep-alive', 'x-amzn-requestid': 'KF9PTCP6V0R4IACB6BSIOF4J7BVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '4250282752'}, 'RetryAttempts': 0}}



'''
