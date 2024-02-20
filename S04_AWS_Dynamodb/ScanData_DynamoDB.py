import boto3
from pprint import pprint

db = boto3.resource('dynamodb',region_name='us-east-1')

table = db.Table('employee')

response = table.scan()

data = response['Items']
pprint(data)
'''
[{'name': 'test', 'age': Decimal('24'), 'emp_id': '2'}, {'name': 'mst', 'age': Decimal('28'), 'emp_id': '1'}, {'name': 'test6', 'age': '31', 'emp_id': '6'}, {'name': 'test5', 'age': '30', 'emp_id': '5'}, {'name': 'test7', 'age': '32', 'emp_id': '7'}, {'name': 'Newname', 'age': '29', 'emp_id': '3'}]

'''