import boto3

s3_client = boto3.client('s3',region_name='us-east-1')

response =  s3_client.get_bucket_policy(Bucket="aswmst123")
print(response['Policy'])

# {"Version":"2012-10-17","Id":"Policy1709608125888","Statement":[{"Sid":"Stmt1709608087569","Effect":"Deny","Principal":"*","Action":"s3:PutObject","Resource":"arn:aws:s3:::aswmst123/*","Condition":{"StringEquals":{"s3:x-amz-server-side-encryption":"AES256"}}},{"Sid":"Stmt1709608553304","Effect":"Deny","Principal":"*","Action":"s3:PutObject","Resource":"arn:aws:s3:::aswmst123/*","Condition":{"Null":{"s3:x-amz-server-side-encryption":"true"}}}]}

