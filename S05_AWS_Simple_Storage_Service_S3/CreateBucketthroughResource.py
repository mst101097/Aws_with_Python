import boto3

bucket = boto3.resource('s3',region_name='us-east-1')

response = bucket.create_bucket(
    Bucket ="testmst123",
    ACL = "private",

    # if you are using default region name us-east-1 then you do not need add this constraints in parameter
    # CreateBucketConfiguration={
    #     'LocationConstraint':'us-east-1'
        
    # }
)

print(response)

# s3.Bucket(name='botolession2')
