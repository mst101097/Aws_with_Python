import boto3

ses_client = boto3.client('ses')

response = ses_client.create_template(
    Template ={
        'TemplateName':'CustomTemplate',
        'SubjectPart' :'Welcome to the AWS Course',
        'TextPart':'Thanks for the Joining us!!',
        'HtmlPart':'Thanks for the joining us!!'
    }
)

print(response)