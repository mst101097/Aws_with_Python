import boto3

db = boto3.client('dynamodb',region_name='us-east-1')

response = db.put_item(

    TableName='employee',

    Item ={
        'emp_id':{
            'S':'3'
        },
        'name':{
            'S':'Newname'
        },
        'age':{
            'S':'29'
        }
    }
)

if response:
    print('data inserted')