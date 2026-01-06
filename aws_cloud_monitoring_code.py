# AWS Cloud Monitoring System
# Python Code (AWS Lambda Function)

import json
import boto3

def lambda_handler(event, context):
    # Log CloudWatch alarm event
    print("CloudWatch Alarm Triggered")
    print(event)

    # Create SNS client
    sns = boto3.client('sns')

    # Publish notification to SNS topic
    sns.publish(
        TopicArn='arn:aws:sns:REGION:ACCOUNT-ID:CloudCPUAlert',
        Message='CPU utilization exceeded the defined threshold. CloudWatch alarm triggered successfully.',
        Subject='AWS Cloud Monitoring Alert'
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent successfully')
    }
