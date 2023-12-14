import boto3

def list_policies():
    iam = boto3.client('iam')

    paginator = iam.get_paginator('list_policies')

    for response in paginator.paginate(Scope="Local"):
        for policy in response['Policies']:
            policy_name =  policy['PolicyName']
            Arn = policy['Arn']

            print(f'Policy Name: {policy_name}, ARN_Name: {Arn}')


list_policies()
'''
Policy Name: AWSLambdaBasicExecutionRole-4c6a6ce6-431f-487d-9921-75f5f9fb877c,
ARN_Name: arn:aws:iam::375253976385:policy/service-role/AWSLambdaBasicExecutionRole-4c6a6ce6-431f-487d-9921-75f5f9fb877c

Policy Name: pyFullAccess, 
ARN_Name: arn:aws:iam::375253976385:policy/pyFullAccess

'''
 