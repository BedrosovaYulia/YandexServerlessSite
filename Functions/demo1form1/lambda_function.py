import os
import json
import boto3

def lambda_handler(event,context):

    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net',
        aws_access_key_id = os.environ['key_id'],
        aws_secret_access_key = os.environ['access_key'],
    )

    # Загрузить объекты в бакет

    ## Из строки
    s3.put_object(Bucket=os.environ['bucket'], Key=event['queryStringParameters']['email'], Body=str(event['queryStringParameters']))


    return{
        'statusCode':200,
        'body':json.dumps('Hello from Yandex Function')
    }