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

            ddb.put_item(
                TableName=os.environ["TABLE"],
                Item={
                    "id":{"S": item["dynamodb"]["NewImage"]["id"]["S"]},
                    "comment": {"S": item["dynamodb"]["NewImage"]["comment"]["S"]},
                    "sentiment": {"S": sentiment["Sentiment"]},
                    "positive": {"N": str(sentiment["SentimentScore"]["Positive"])},
                    "negative": {"N": str(sentiment["SentimentScore"]["Negative"])},
                    "neutral": {"N": str(sentiment["SentimentScore"]["Neutral"])},
                    "mixed": {"N": str(sentiment["SentimentScore"]["Mixed"])}
                }
            )
    except Exception as e:
        print(e)
    return True