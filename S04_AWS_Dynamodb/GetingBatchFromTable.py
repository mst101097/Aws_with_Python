import boto3
from pprint import pprint

db =  boto3.resource('dynamodb',region_name='us-east-1')

response =  db.batch_get_item(
    RequestItems={
        'employee':{
            'Keys':[
                {
                    'emp_id':'1'
                },
                {
                    'emp_id':'2'
                },
                {
                    'emp_id':'3'
                }
            ]
        }
    }
)

pprint(response['Responses'])
'''
{'employee': [{'age': '29', 'emp_id': '3', 'name': 'Newname'},
              {'age': Decimal('28'), 'emp_id': '1', 'name': 'mst'},
              {'age': Decimal('24'), 'emp_id': '2', 'name': 'test'}]}

'''