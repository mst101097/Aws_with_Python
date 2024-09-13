import boto3

def lambda_handler(event,context):
    db = boto3.resource('dynamodb')

    table  = db.table('Users')

    with table.batch_writer() as batch:
        batch.put_item(
            Item ={
                'id':1,
                'name':'mst',
                'age':'25'
            }
        ),
        batch.put_item(
            Item ={
                'id':1,
                'name':'mst',
                'age':'25'
            }
        )




