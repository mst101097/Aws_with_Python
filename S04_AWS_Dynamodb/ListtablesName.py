import boto3

db = boto3.client('dynamodb',region_name='us-east-1')

response =  db.list_tables()

print(response['TableNames'])
print(response)
