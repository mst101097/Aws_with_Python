import boto3


def send_html_email():
    ses_client = boto3.client('ses')
    CHARSET="UTF-8"
    html_email_content= """
        <html>
            <head></head>
            <h1 style='text_align:center'>AWS with Python & Boto3</h1>
            <p style='color:red'>Welcome to the course and thanks for buying the course</p>
        </html>
    
    """


    response = ses_client.send_email(
        Destination={
            "ToAddresses":[
                "mca1719214876@gmail.com",
            ]
        },
        Message={
            "Body":{
                "Html":{
                    "Charset":CHARSET,
                    "Data":html_email_content
                }
            },
            "Subject":{
                "Charset":CHARSET,
                "Data":"AWS Course with Python"
            }
        },
        Source="mca1719214876@gmail.com"
    )

    print(response)


send_html_email()


# {'MessageId': '010001929a27bb13-a5c299ae-5eed-4130-bdee-1f8b153fc0bf-000000', 'ResponseMetadata': {'RequestId': 'd73f6995-8893-4a6f-b5f2-dc1ff3d79223', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Thu, 17 Oct 2024 11:05:48 GMT', 'content-type': 'text/xml', 'content-length': '326', 'connection': 'keep-alive', 'x-amzn-requestid': 'd73f6995-8893-4a6f-b5f2-dc1ff3d79223'}, 'RetryAttempts': 0}}
