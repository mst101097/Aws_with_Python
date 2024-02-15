import boto3

db = boto3.resource('dynamodb',region_name='us-east-1')
# db = boto3.client('dynamodb', region_name='us-east-1')

table = db.Table('employee')

table.put_item(
    Item={
        "emp_id":"1",
        "name":"mst",
        "age":28
    }
    
)
'''
Item={
        "emp_id":"2",
        "name":"test",
        "age":24
    }
'''