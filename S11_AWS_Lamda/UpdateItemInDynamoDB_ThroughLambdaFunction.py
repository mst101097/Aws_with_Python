import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event,context):
    db = boto3.resource('dynamodb')

    table  = db.Table('Users')

    table.update_item(
        Key={
            'id':1
        },
        UpdateExpression ="set age = :g",
        ExpressionAttributeValues={
            ':g':45
        },
        ReturnValues="UPDATED_NEW"
    )
'''
Function Logs
START RequestId: eb0dc491-077a-422d-86cf-b99292030871 Version: $LATEST
END RequestId: eb0dc491-077a-422d-86cf-b99292030871
REPORT RequestId: eb0dc491-077a-422d-86cf-b99292030871	Duration: 2860.29 ms	Billed Duration: 2861 ms	Memory Size: 128 MB	Max Memory Used: 76 MB	Init Duration: 304.34 ms

'''