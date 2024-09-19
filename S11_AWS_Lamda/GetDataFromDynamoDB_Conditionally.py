import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event,context):
    db = boto3.resource('dynamodb')

    table  = db.Table('Users')

    response = table.query(
        KeyConditionExpression = Key('id').eq(1)
    )

    if 'Items' in response:
        print(response['Items'][0])
'''
START RequestId: ff80c6f9-3745-4d9d-b4c1-da8872f5f71a Version: $LATEST
{'id': Decimal('1'), 'name': 'mst', 'age': '25'}
END RequestId: ff80c6f9-3745-4d9d-b4c1-da8872f5f71a
REPORT RequestId: ff80c6f9-3745-4d9d-b4c1-da8872f5f71a	Duration: 2585.76 ms	Billed Duration: 2586 ms	Memory Size: 128 MB	Max Memory Used: 76 MB	Init Duration: 294.00 ms

'''