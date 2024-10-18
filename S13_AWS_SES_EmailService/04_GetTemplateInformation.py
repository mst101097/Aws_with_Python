import boto3
from pprint import pprint

ses_client = boto3.client('ses')
'''
#Get all the list of templates

response = ses_client.list_templates()
pprint(response)

'''

#get templates infromations
response = ses_client.get_template(
    TemplateName = 'CustomTemplate'
)

pprint(response)

pprint(response['Template'])

'''
'Template': {'HtmlPart': 'Thanks for the joining us!!',
              'SubjectPart': 'Welcome to the AWS Course',
              'TemplateName': 'CustomTemplate',
              'TextPart': 'Thanks for the Joining us!!'}}
''' 