import boto3

def lambda_handler(event,context):
    db = boto3.resource('dynamodb')

    table  = db.Table('Users')

    response = table.delete_item(
        Key ={
            'id':1
        }
    )

    print(response)

'''
Function Logs
START RequestId: 9b8b15d0-f9ab-4bf2-82a9-fe4158b1ab80 Version: $LATEST
{'ResponseMetadata': {'RequestId': 'VLCKN0J1SK7VF56FO6J4I49C8BVV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'Server', 'date': 'Thu, 19 Sep 2024 10:18:10 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '2', 'connection': 'keep-alive', 'x-amzn-requestid': 'VLCKN0J1SK7VF56FO6J4I49C8BVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '2745614147'}, 'RetryAttempts': 0}}
END RequestId: 9b8b15d0-f9ab-4bf2-82a9-fe4158b1ab80
REPORT RequestId: 9b8b15d0-f9ab-4bf2-82a9-fe4158b1ab80	Duration: 2818.48 ms	Billed Duration: 2819 ms	Memory Size: 128 MB	Max Memory Used: 76 MB	Init Duration: 326.14 ms

Request ID
'''