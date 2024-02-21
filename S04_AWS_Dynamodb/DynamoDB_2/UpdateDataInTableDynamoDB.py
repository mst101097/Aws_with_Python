import boto3
from decimal import Decimal
from pprint import pprint

def update_movie(title,year,rating,plot,dynamodb=None):
    if not dynamodb:
        dynamodb= boto3.resource('dynamodb',region_name='us-east-1')
    
    table = dynamodb.Table('Movies')

    response = table.update_item(
        Key={
            'year':year,
            'title':title,
        },
        UpdateExpression="set info.rating=:r, info.plot=:p",
        ExpressionAttributeValues={
            ':r':Decimal(rating),
            ':p':plot,

        },

        ReturnValues='UPDATED_NEW'
    )

    return response

if __name__=="__main__":
    update_response=update_movie(
        "Insidious: Chapter 2",2013, 5.0 ,"This is updated"
    )

    pprint(update_response)

'''
{'Attributes': {'info': {'plot': 'This is updated', 'rating': Decimal('5')}},
 'ResponseMetadata': {'HTTPHeaders': {'connection': 'keep-alive',
                                      'content-length': '81',
                                      'content-type': 'application/x-amz-json-1.0',
                                      'date': 'Wed, 21 Feb 2024 03:49:05 GMT',
                                      'server': 'Server',
                                      'x-amz-crc32': '2647421436',
                                      'x-amzn-requestid': '376B5545GFH97OTRMA35SH5DS3VV4KQNSO5AEMVJF66Q9ASUAAJG'},
                      'HTTPStatusCode': 200,
                      'RequestId': '376B5545GFH97OTRMA35SH5DS3VV4KQNSO5AEMVJF66Q9ASUAAJG',
                      'RetryAttempts': 0}}

'''