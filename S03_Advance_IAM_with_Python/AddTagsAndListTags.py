import boto3

iam_client = boto3.client('iam')

# user_name = 'testscript'

# tags = [{'Key':'Department','Value':'HR'},{'Key':'Project','Value':'Onboarding'}]

# iam_client.tag_user(UserName = user_name,Tags = tags)

# print('tags added')

# ---------------------------------------------- List tags--------

# response = iam_client.list_users()

# for user in response['Users']:
#     user_name = user['UserName']
#     tags =  iam_client.list_user_tags(UserName=user_name)['Tags']
#     print(f"Tags list :{tags}")

'''
Tags list :[{'Key': 'Department', 'Value': 'HR'}, {'Key': 'Project', 'Value': 'Onboarding'}, {'Key': 'AKIAZLIUYTA5WX3RQTPM', 'Value': 'fortesstscript'}]

'''

# -----------------------------Remove tags---------------------------------

user_name = 'testscript'

tag_keys = ['Department','Project']

respone = iam_client.untag_user(UserName=user_name,TagKeys=tag_keys)
print(respone)
'''
{'ResponseMetadata': {'RequestId': 'af337255-3b7d-4fed-8c05-6c1bac63b600', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'af337255-3b7d-4fed-8c05-6c1bac63b600', 'content-type': 'text/xml', 'content-length': '198', 'date': 'Mon, 08 Jan 2024 13:37:31 GMT'}, 'RetryAttempts': 0}}


'''