import boto3

db = boto3.resource('dynamodb',region_name='us-east-1')

table = db.Table('employee')

response = table.get_item(
    Key = {
        'emp_id':"5"
    }
)


print(response['Item'])


