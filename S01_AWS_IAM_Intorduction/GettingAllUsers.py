import boto3

def getAllUsers():

    iam = boto3.client('iam')

    paginator = iam.get_paginator('list_users')

    for response in paginator.paginate():
        for user in response['Users']:
            username = user['UserName']
            arn = user['Arn']
            print(f'Username:{username} Arn :{arn}')

getAllUsers()

'''
Username:newuser Arn :arn:aws:iam::375253976385:user/newuser
Username:testuser_script Arn :arn:aws:iam::375253976385:user/testuser_script
Username:testuser_script2 Arn :arn:aws:iam::375253976385:user/testuser_script2
'''