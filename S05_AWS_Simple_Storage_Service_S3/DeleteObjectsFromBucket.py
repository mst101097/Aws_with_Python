import boto3

client = boto3.client('s3',region_name='us-east-1')

response = client.delete_object(
    Bucket = '01-mstbucketfortest',
    Key ='copied.pdf'

)


print(response)


# {'ResponseMetadata': {'RequestId': 'KYD5Y37XHYAD2E7Z', 'HostId': 'toH3l79MyTprM2A6rA8S4go+zCKfN7OhKuNjPZ1KWuY0fnfOpflmdEr/XB+wEEseMc/L+Rnl4Z5+MrxYX6EAzMggOLJ7kOucXy/yg5ndyoM=', 'HTTPStatusCode': 204, 'HTTPHeaders': {'x-amz-id-2': 'toH3l79MyTprM2A6rA8S4go+zCKfN7OhKuNjPZ1KWuY0fnfOpflmdEr/XB+wEEseMc/L+Rnl4Z5+MrxYX6EAzMggOLJ7kOucXy/yg5ndyoM=', 'x-amz-request-id': 'KYD5Y37XHYAD2E7Z', 'date': 'Fri, 01 Mar 2024 03:50:41 GMT', 'server': 'AmazonS3'}, 'RetryAttempts': 0}}

# if you want to delete multiple files from bucket

response = client.delete_objects(
    Bucket='botolession2',
    Delete={
        'Objects':[
            {
                'Key':'file.pdf'
            },
            {
                'Key':'myfile.txt'
            }
        ]
    }
)
