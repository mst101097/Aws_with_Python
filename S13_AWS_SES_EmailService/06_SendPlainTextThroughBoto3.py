import boto3
from pprint import pprint


def sendPlainText():
    ses_client = boto3.client('ses')
    CHARSET = 'UTF-8'

    response = ses_client.send_email(
        Destination ={
            "ToAddresses":[
                "mca1719214876@gmail.com",
            ]
        },
        Message ={
            "Body":{
                "Text":{
                    "Charset":CHARSET,
                    "Data":"Thanks for the joining the course"
                }
            },
            "Subject":{
                "Charset":CHARSET,
                "Data":"AWS Course Email"
            }

        },
        Source = "mca1719214876@gmail.com",
    )

    print(response)

sendPlainText()