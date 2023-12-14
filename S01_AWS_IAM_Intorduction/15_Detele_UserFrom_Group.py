import boto3

def Delete_userFrom_group(username,group_name):
    iam = boto3.resource('iam')

    group = iam.Group(group_name)

    response =  group.remove_user(
        UserName=username
    )

    print(response)

Delete_userFrom_group('newuser','RDSAdmin')
'''
$ python 15_Detele_UserFrom_Group.py
{'ResponseMetadata': {'RequestId': '9358922e-4d45-4bc0-a36e-3371eacd39de', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '9358922e-4d45-4bc0-a36e-3371eacd39de', 'content-type': 'text/xml', 'content-length': '218', 'date': 'Thu, 14 Dec 2023 14:25:50 GMT'}, 'RetryAttempts': 0}}

'''

'''


def delete_user_from_group(username, group_name):
    iam = boto3.resource('iam')

    # Get the IAM group
    group = iam.Group(group_name)

    # Remove the user from the group
    response = group.remove_user(
        UserName=username
    )

    print(response)

delete_user_from_group('newuser', 'RDSAdmin')
'''

