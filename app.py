import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('ec2')
    response = client.run_instances(
    ImageId='ami-076c6dbba59aa92e6',
    InstanceType='t2.micro',
    KeyName='Cust-KeyPair',
    MaxCount=1,
    MinCount=1,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
<<<<<<< HEAD
                    'Value': 'server_from_lambda_git'
=======
                    'Value': 'server_from_lambda_boto3'
>>>>>>> 5481b05e8458be9ee4ad15d4bba3e35217b77c40
                },
            ]
        },
    ]
)

