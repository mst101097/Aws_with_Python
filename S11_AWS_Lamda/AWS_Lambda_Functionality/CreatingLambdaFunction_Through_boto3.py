import boto3

iamClient = boto3.client('iam')
lambdaClient = boto3.client('lambda')

with open('lambda.zip','rb') as f:
    zipped_code = f.read()

role = iamClient.get_role(RoleName = 'PyLambdaBasicExecution')

response = lambdaClient.create_function(
    FunctionName = 'HelloLambdaFunction',
    Runtime='python3.12',
    Role=role['Role']['Arn'],
    Handler = 'lambda_function.lambda_handler',
    Code = dict(ZipFile=zipped_code),
    Timeout=300
)

print(response)

'''
{'ResponseMetadata': {'RequestId': '09fa2fc4-da6b-4f9f-b864-ec826537478e', 'HTTPStatusCode': 201, 'HTTPHeaders': {'date': 'Thu, 19 Sep 2024 11:05:54 GMT', 'content-type': 'application/json', 'content-length': '1352', 'connection': 'keep-alive', 'x-amzn-requestid': '09fa2fc4-da6b-4f9f-b864-ec826537478e'}, 'RetryAttempts': 0}, 'FunctionName': 'HelloLambdaFunction', 'FunctionArn': 'arn:aws:lambda:us-east-1:375253976385:function:HelloLambdaFunction', 'Runtime': 'python3.12', 'Role': 'arn:aws:iam::375253976385:role/PyLambdaBasicExecution', 'Handler': 'lambda_function.lambda_handler', 'CodeSize': 439, 'Description': '', 'Timeout': 300, 'MemorySize': 128, 'LastModified': '2024-09-19T11:05:54.305+0000', 'CodeSha256': 'uKOU7aLu7HBCi5yIHLnsBEkvPLSgVd4itz4qshRWbzQ=', 'Version': '$LATEST', 'TracingConfig': {'Mode': 'PassThrough'}, 'RevisionId': 'cb2e8947-ef95-4806-8b0e-09884fd45a43', 'State': 'Pending', 'StateReason': 'The function is being created.', 'StateReasonCode': 'Creating', 'PackageType': 'Zip', 'Architectures': ['x86_64'], 'EphemeralStorage': {'Size': 512}, 'SnapStart': {'ApplyOn': 'None', 'OptimizationStatus': 'Off'}, 'RuntimeVersionConfig': {'RuntimeVersionArn': 'arn:aws:lambda:us-east-1::runtime:acd6500d0e3f6a085fb07933e3472ed6e58360d19ec5dd91bc7c7e8ad119de42'}, 'LoggingConfig': {'LogFormat': 'Text', 'LogGroup': '/aws/lambda/HelloLambdaFunction'}}


'''