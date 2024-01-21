import boto3
import json
from datetime import datetime

iam =  boto3.client('iam')

# current_date = datetime.now().strftime('%Y-%m-%d')

# start_time= f"{current_date} T01:00:00Z"
# end_time = f"{current_date} T03:00:00Z"

# from datetime import datetime

current_date = datetime.now().strftime('%Y-%m-%d')

start_time = f"{current_date}T01:00:00Z"
end_time = f"{current_date}T03:00:00Z"


policy_document = {
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect":"Allow",
            "Action":"s3:GetObject",
            "Resource":"arn:aws:s3:::01-mstbucketfortest/*",
            "Condition":{
                "DateGreaterThan":{"aws:CurrentTime":start_time},
                "DateLessThan":{"aws:CurrentTime":end_time}
            }
        }
    ]
}

response = iam.create_policy(
    PolicyName ='AccessWindowPolicyNew',
    PolicyDocument = json.dumps(policy_document)
)

print(response)
'''
{'Policy': {'PolicyName': 'AccessWindowPolicyNew', 'PolicyId': 'ANPAZLIUYTA5QQ7W7NWY4', 'Arn': 'arn:aws:iam::642678036539:policy/AccessWindowPolicyNew', 'Path': '/', 'DefaultVersionId': 'v1', 'AttachmentCount': 0, 'PermissionsBoundaryUsageCount': 0, 'IsAttachable': True, 'CreateDate': datetime.datetime(2024, 1, 8, 13, 14, 15, tzinfo=tzutc()), 'UpdateDate': datetime.datetime(2024, 1, 8, 13, 14, 15, tzinfo=tzutc())}, 'ResponseMetadata': {'RequestId': '9c91125e-3573-438d-b809-265f5f4b63ff', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '9c91125e-3573-438d-b809-265f5f4b63ff', 'content-type': 'text/xml', 'content-length': '777', 'date': 'Mon, 08 Jan 2024 13:14:15 GMT'}, 'RetryAttempts': 0}}

'''w