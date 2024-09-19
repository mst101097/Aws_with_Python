import boto3
import json

iam = boto3.client('iam')

role_policy ={
    "Version":"2012-10-17",
    "Statement":[
        {
            "Sid":"",
            "Effect":"Allow",
            "Principal":{
                "Service":"lambda.amazonaws.com"
            },
            "Action":"sts:AssumeRole"
        }
    ]
}

response = iam.create_role(
    RoleName = 'PyLambdaBasicExecution',
    AssumeRolePolicyDocument=json.dumps(role_policy)
)

print(response)

'''
{'Role': {'Path': '/', 'RoleName': 'PyLambdaBasicExecution', 'RoleId': 'AROAVOXXBIVAXS3TOI7EF', 'Arn': 'arn:aws:iam::375253976385:role/PyLambdaBasicExecution', 'CreateDate': datetime.datetime(2024, 9, 19, 10, 45, 32, tzinfo=tzutc()), 'AssumeRolePolicyDocument': {'Version': '2012-10-17', 'Statement': [{'Sid': '', 'Effect': 'Allow', 'Principal': {'Service': 'lambda.amazonaws.com'}, 'Action': 'sts:AssumeRole'}]}}, 'ResponseMetadata': {'RequestId': '0b2fd4cb-1615-42a9-8eda-d69d0640ce3d', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Thu, 19 Sep 2024 10:45:32 GMT', 'x-amzn-requestid': '0b2fd4cb-1615-42a9-8eda-d69d0640ce3d', 'content-type': 'text/xml', 'content-length': '825'}, 'RetryAttempts': 0}}

'''