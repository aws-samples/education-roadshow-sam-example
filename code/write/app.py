# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import os
import json
import boto3
import uuid

ddb = boto3.client('dynamodb')

def lambda_handler(event, context):
    uid = uuid.uuid4()
    body = json.loads(event['body'])
    response = {"success": False}
    try:
        ddb.put_item(
            TableName=os.environ["TABLE"],
            Item={
                "id":{"S": str(uid)},
                "comment": {"S": body['comment']}
            }
        )
        response = {"success": True}
    except Exception as e:
        print(e)
    return {
        "statusCode": 200,
        "body": json.dumps(response),
    }
