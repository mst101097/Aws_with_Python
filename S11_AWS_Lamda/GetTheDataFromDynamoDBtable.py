import boto3

def lambda_handler(event,context):
    db = boto3.resource('dynamodb')

    response  = db.batch_get_item(
        RequestItems={
            'Users':{
                'Keys':[
                    {
                        'id':1
                    },
                    {
                        'id':2
                    }
                ]
            }
        }
    )
    print(response)

'''
START RequestId: 5a8fe464-762c-4c7c-86ac-cf5554809567 Version: $LATEST
{'Responses': {'Users': [{'id': Decimal('1'), 'name': 'mst', 'age': '25'}, {'id': Decimal('2'), 'name': 'mst', 'age': '25'}]}, 'UnprocessedKeys': {}, 'ResponseMetadata': {'RequestId': 'Q9P4FS5HFGEQSVT2REGV0EB273VV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'Server', 'date': 'Thu, 19 Sep 2024 09:53:05 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '152', 'connection': 'keep-alive', 'x-amzn-requestid': 'Q9P4FS5HFGEQSVT2REGV0EB273VV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '2662354517'}, 'RetryAttempts': 0}}
END RequestId: 5a8fe464-762c-4c7c-86ac-cf5554809567
REPORT RequestId: 5a8fe464-762c-4c7c-86ac-cf5554809567	Duration: 2537.48 ms	Billed Duration: 2538 ms	Memory Size: 128 MB	Max Memory Used: 75 MB	Init Duration: 297.43 ms
'''