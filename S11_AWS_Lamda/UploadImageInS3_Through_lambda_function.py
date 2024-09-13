import boto3

def lambda_handler(event, context):
    client =  boto3.client('s3')

    with open('aws.png','rb') as f:
        data =  f.read()
    
    response = client.put_object(
        Bucket = "may-learningaws-block",
        Body = data,
        key = "aws.png"
    )

    print(response)