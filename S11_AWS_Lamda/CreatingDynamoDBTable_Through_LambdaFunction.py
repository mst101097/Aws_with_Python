import boto3

def lambda_handler(event,context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table (
        TableName = 'Users',
        KeySchema =[
            {
                'AttributeName':'id',
                'KeyType':'HASH'
            }
        ],
        AttributeDefinitions = [
            {
            'AttributeName':'id',
            'AttributeType':'N'
            }
        ],
        ProvisionedThroughput ={
            'ReadCapacityUnit' : 3,
            'WriteCapacityUnits': 3
        }      
    )
    print("Table status ",table.table_status)