import boto3

db = boto3.resource('dynamodb',region_name='us-east-1')

table = db.Table('employee')

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            "emp_id":"5",
            "name":"test5",
            "age":'30'
    }
    )

    batch.put_item(
        Item={
            "emp_id":"6",
            "name":"test6",
            "age":'31'
    }
    )
    batch.put_item(
        Item={
            "emp_id":"7",
            "name":"test7",
            "age":'32'
    }
    )

print('datainserted')