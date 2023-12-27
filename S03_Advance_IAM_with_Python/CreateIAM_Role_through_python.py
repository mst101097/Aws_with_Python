import boto3
import json

iam  = boto3.client('iam')

role_name = "MyNewEC2Role"

trust_policy = {
    "Version":"2012-10-17",
    "Statement":[
        {
            "Effect":"Allow",
            "Principal":{
                "Service":"ec2.amazonaws.com"
            },
            "Action":"sts:AssumeRole"
        }
    ]
}

response = iam.create_role(
    RoleName = role_name,
    AssumeRolePolicyDocument=json.dumps(trust_policy)
)


print(response)
'''

{'Role': {'Path': '/', 'RoleName': 'MyNewEC2Role', 'RoleId': 'AROAZLIUYTA5QVU3UDHOE', 'Arn': 'arn:aws:iam::642678036539:role/MyNewEC2Role', 'CreateDate': datetime.datetime(2023, 12, 18, 6, 7, 45, tzinfo=tzutc()), 'AssumeRolePolicyDocument': {'Version': '2012-10-17', 'Statement': [{'Effect': 'Allow', 'Principal': {'Service': 'ec2.amazonaws.com'}, 'Action': 'sts:AssumeRole'}]}}, 'ResponseMetadata': {'RequestId': '29d5491c-bf69-4751-b2af-9d76e695c6c3', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '29d5491c-bf69-4751-b2af-9d76e695c6c3', 'content-type': 'text/xml', 'content-length': '775', 'date': 'Mon, 18 Dec 2023 06:07:44 GMT'}, 'RetryAttempts': 0}}

52329058@NODLTP52329058 MINGW64 ~/Desktop/Python
'''