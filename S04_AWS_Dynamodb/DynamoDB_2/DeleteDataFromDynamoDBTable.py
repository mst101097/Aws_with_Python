import boto3
from pprint import pprint
from botocore.exceptions import ClientError


def delete_movie(title,year,dynamodb=None):

    if not dynamodb:
            dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
        
    table = dynamodb.Table('Movies')

    try:
        response = table.delete_item(
            Key={
                'year':year,
                'title':title
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    
    
    else:
        return response

if __name__=='__main__':
    delete_response = delete_movie("Now You See Me",2013) 
    if delete_response:
        pprint(delete_response)



# {'ResponseMetadata': {'HTTPHeaders': {'connection': 'keep-alive',
#                                       'content-length': '2',
#                                       'content-type': 'application/x-amz-json-1.0',
#                                       'date': 'Thu, 22 Feb 2024 03:12:32 GMT',
#                                       'server': 'Server',
#                                       'x-amz-crc32': '2745614147',
#                                       'x-amzn-requestid': '52FUR7RLLP5LQN40LJFST8VO73VV4KQNSO5AEMVJF66Q9ASUAAJG'},
#                       'HTTPStatusCode': 200,
#                       'RequestId': '52FUR7RLLP5LQN40LJFST8VO73VV4KQNSO5AEMVJF66Q9ASUAAJG',
#                       'RetryAttempts': 0}}
