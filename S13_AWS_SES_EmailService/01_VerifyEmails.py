import boto3

ses_client = boto3.client('ses')

response = ses_client.verify_email_address(
    EmailAddress='mca1719214876@gmail.com'
)

print(response)