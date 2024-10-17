import boto3
from pprint import pprint

lambda_client = boto3.client('lambda')

response = lambda_client.get_function(
    FunctionName = 'HelloLambdaFunction'
)

pprint(response)
'''
{'Code': {'Location': 'https://prod-04-2014-tasks.s3.us-east-1.amazonaws.com/snapshots/375253976385/HelloLambdaFunction-17509708-b25e-48c7-8763-ce389ab252e9?versionId=vrsB7ltqiIfQqhiqPFCJ14JkJhMMFp.F&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLWVhc3QtMSJHMEUCIDxHcK%2FfQewMrdgz6VYseIiTpaxdXr3NztoMYKzedS9QAiEAoKy5ETCXCK73M%2BvT6%2BMFMwDqAHSEpZlNbdqwZPKtetkqsgUIdRAAGgw3NDk2Nzg5MDI4MzkiDJx7NYzwnXdEObOx1CqPBTtwgxEGz1yK12T7SV7vznDQW3hGaBMzI43Hz2fRiadWt%2BfIOfKdsCc9IQlDf4OZXNMJQXi2e9BXywUxJaDTI70ExhE8XyhrjErK5l5qj978A9U7x0ZJbed3o523yUEdBQx0aEXnM%2BqyTY5RlO4BDbQRTLAyQKDSDsAG%2BidfQfGKky3WeWWjmQeXBefHrC%2FldfAYsvw9Wb%2F3ro1goBfmiyWsaAIa2LLJnE21L0onIjzo6fyr8sR%2FLYdhWUye2WQCjqkJV0dqeiDwX9xthmjRzScbmH2dWTVZxMvVkcJ5Hnd2tWcfJdI2MbnrPcfNkobWmO4DokMpTZ0wuR%2FvLSrBqocR%2Bj%2F1GawLOa3ahGZAsD2xr7GeTO%2Bgv5%2Bosq7BLB7PW38MQmdbX7mSHkNaUQ9Xjg5UlH8sr%2F6dUQtpc2HQ%2FiYdhzE9sbZ5d0w%2Bws%2B9qKt%2BOfOacl7LScyhZV6rbc0t1sUP%2FdaY79QJnWDIguuXXfKswkA0YZouMHVqeYJXZw1RAi6iv4oAaVofB7ipEwUCa5gvo4KpLpiLCIKQOO0KJZPf0szesFzu3gFJ%2B754%2B4ypPDPL7Ly2QymdL3bKQOF9P0CP%2FRomS915p38OM%2BZmgwZ4DnC7Obti6%2BebiaPWYTRD8JWMK8myezo97Yz4GJD6Q0gel8HQvaP%2FnAZClXwysnZrnBq3Hi4olWNo1ODHihcLT9sui7ibVhafaEfYRCmDjR06jQarZSOmmwyDA3QqNRbEQ%2BYmUbYg7uPNhlXvn5XAmpa80Xb58Izg94Pad9XYVdMa47Stb8JFiidTzGtD3MJA66oVzb%2FkpszLeFuajP0aY5IaItUvF7QGAaWo9KN0%2BM4evzYZgZGAJS8o1KWcCUcwtrm1twY6sQEd3qmVRpz%2Bw6lcNGalF4313HaoA0FhVZUT1KSNi%2BOuV0zsr2jMkulWJ6KhDzW6GSW9rQT%2BharkoKtr9P1%2FREsFNkj54bSXlEja1%2FVtt3OTtIo1xFxmDWB3wUz4TQZdyJs09p4IU39sC4fri%2FMF7Ebo8GmDyIWLiic9ujilQCTWFNxl9jqk0KHUKoOvj%2FwLMv1bAh7gUbFv3cSfQ6mvIEw98URMa2S9YTKBRlpVqFkxgyU%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240920T122622Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Credential=ASIA25DCYHY3SVYHKGNE%2F20240920%2Fus-east-1%2Fs3%2Faws4_request&',
          'RepositoryType': 'S3'},
 'Configuration': {'Architectures': ['x86_64'],
                   'CodeSha256': 'qdCtCVEGwIx5tsshyScikccJ23lxDb22QKRQLYEvrfA=',
                   'CodeSize': 352,
                   'Description': '',
                   'EphemeralStorage': {'Size': 512},
                   'FunctionArn': 'arn:aws:lambda:us-east-1:375253976385:function:HelloLambdaFunction',
                   'FunctionName': 'HelloLambdaFunction',
                   'Handler': 'lambda_function.lambda_handler',
                   'LastModified': '2024-09-19T11:07:46.000+0000',
                   'LastUpdateStatus': 'Successful',
                   'LoggingConfig': {'LogFormat': 'Text',
                                     'LogGroup': '/aws/lambda/HelloLambdaFunction'},
                   'MemorySize': 128,
                   'PackageType': 'Zip',
                   'RevisionId': 'a730718d-0544-46e9-b1cb-fc835e63f879',
                   'Role': 'arn:aws:iam::375253976385:role/PyLambdaBasicExecution',
                   'Runtime': 'python3.12',
                   'RuntimeVersionConfig': {'RuntimeVersionArn': 'arn:aws:lambda:us-east-1::runtime:acd6500d0e3f6a085fb07933e3472ed6e58360d19ec5dd91bc7c7e8ad119de42'},
                   'SnapStart': {'ApplyOn': 'None',
                                 'OptimizationStatus': 'Off'},
                   'State': 'Active',
                   'Timeout': 300,
                   'TracingConfig': {'Mode': 'PassThrough'},
                   'Version': '$LATEST'},
 'ResponseMetadata': {'HTTPHeaders': {'connection': 'keep-alive',
                                      'content-length': '3353',
                                      'content-type': 'application/json',
                                      'date': 'Fri, 20 Sep 2024 12:26:22 GMT',
                                      'x-amzn-requestid': 'e913db2d-c430-47c0-9089-d44c26e67341'},
                      'HTTPStatusCode': 200,
                      'RequestId': 'e913db2d-c430-47c0-9089-d44c26e67341',
                      'RetryAttempts': 0}}




'''