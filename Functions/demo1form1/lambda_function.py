import os
import json
import boto3

def lambda_handler(event,context):

    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net',
        aws_access_key_id = '*****************',
        aws_secret_access_key = '**************************************',
    )

    
    #save data
    s3.put_object(Bucket='ybwsstorage1', Key=event['queryStringParameters']['email'], Body=str(event['queryStringParameters']))


    return{
        'statusCode':200,
        'body':json.dumps('Hello from Yandex Function')
    }