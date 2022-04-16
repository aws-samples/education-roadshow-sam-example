# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import os
import boto3

ddb = boto3.client('dynamodb')
comp = boto3.client('comprehend')

def lambda_handler(event, context):
    print(event)
    try:
        for item in event['Records']:
            sentiment = comp.detect_sentiment(
                Text=item["dynamodb"]["NewImage"]["comment"]["S"],
                LanguageCode='en'
            )

            ddb.update_item(
                TableName=os.environ["TABLE"],
                Key={"id":{"S": item["dynamodb"]["NewImage"]["id"]["S"]}},
                UpdateExpression="SET #sent=:sent",
                ExpressionAttributeNames={
                    "#sent": "sentiment"
                },
                ExpressionAttributeValues={
                    ":sent": {"S": sentiment["Sentiment"]}
                }
            )
    except Exception as e:
        print(e)
    return True