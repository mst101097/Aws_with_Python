import boto3

# Create an IAM client
iam = boto3.client('iam')

try:
    response = iam.list_users()
    print("Users:")
    for user in response['Users']:
        print(f" - {user['UserName']}")
except Exception as e:
    print(e)