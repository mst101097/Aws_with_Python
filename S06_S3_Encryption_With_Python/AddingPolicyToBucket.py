import boto3
import json

bucket_name ="aswmst123"

bucket_policy = {
    "Version": "2012-10-17",
    "Id": "Policy1709608125888",
    "Statement": [
        {
            "Sid": "Stmt1709608087569",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:PutObject",
            "Resource": f'arn:aws:s3:::{bucket_name}/*',
            "Condition": {
                "StringEquals": {
                    "s3:x-amz-server-side-encryption": "AES256"
                }
            }
        },
        {
            "Sid": "Stmt1709608553304",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:PutObject",
            "Resource": f'arn:aws:s3:::{bucket_name}/*',
            "Condition": {
                "Null": {
                    "s3:x-amz-server-side-encryption": "true"
                }
            }
        } 
    ]
}

bucket_policy =  json.dumps(bucket_policy)

s3_client = boto3.client('s3',region_name='us-east-1')
response =  s3_client.put_bucket_policy(Bucket=bucket_name,Policy=bucket_policy)
print(response)


# {'ResponseMetadata': {'RequestId': '72XXZATZ1V9H70JX', 'HostId': 'ruxm36UnweIsgNJAU4c9DTtHdaOkNWU2fJtzTL1F6ECKqJS9Wo4H/yxTpdoPxRuUIAw/fGOikf8=', 'HTTPStatusCode': 204, 'HTTPHeaders': {'x-amz-id-2': 'ruxm36UnweIsgNJAU4c9DTtHdaOkNWU2fJtzTL1F6ECKqJS9Wo4H/yxTpdoPxRuUIAw/fGOikf8=', 'x-amz-request-id': '72XXZATZ1V9H70JX', 'date': 'Mon, 11 Mar 2024 03:22:53 GMT', 'server': 'AmazonS3'}, 'RetryAttempts': 0}}















