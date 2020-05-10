import boto3
import json

def lambda_handler(event, context):
    ec2Client = boto3.client('ec2')

    regionRes = ec2Client.meta.region_name
    print("OK")
    return {
        'statusCode': 200,
        'body': json.dumps(regionRes)
    }
